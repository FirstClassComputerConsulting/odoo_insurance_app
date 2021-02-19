# -*- coding: utf-8 -*-
from odoo import models, fields, api

import pika
import json
import time


class rabbitmq(models.Model):
    _name = 'res.partner'
    _description = 'Processing of Contact Records'
    _inherit = "res.partner"

    def sequential_contacts(self):
        records = self.env['res.partner'].search([])
        for record in records:
            self.process_contact(record)

    
    def process_contacts(self):
        connection, channel = self.get_connection()

        records = self.env['res.partner'].search([])
        for record in records:
            
            rec = {'id':record.id, 'name': record.name}
            # Publish it to RabbitMQ
            channel.basic_publish(exchange='',
                            routing_key='process_contact',
                            body=json.dumps(rec))
            # REFACTOR/MOVE TO CALLBACK METHOD
            print(" [x] Sent '"+ record.name+ " '")
        
        connection.close()

    # Slow methods / processes / API / Nested Loops / Bad Code / Sad Code / Etc.
    def process_contact(self,rec):
        print(rec)
        time.sleep(1)

    def process_queue(self):
        connection, channel = self.get_connection()


        # PROCESS CONTACT - Anything on the queue needing to be called is moved here
        def callback(ch, method, properties, body):
            #print(body)
            if body:
                try:
                    rec = json.loads(body)
                    self.process_contact(rec)
                    print(" [x] Received %r" % rec)
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                except:
                    print("error loading json")

        # Process the callback       
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume('process_contact', callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
        



    def get_connection(self):
        credentials = pika.PlainCredentials(username='mojo', password='mojo')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="168.235.109.177",port=5672,credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='process_contact', durable=True)
        return connection,channel

    #name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
