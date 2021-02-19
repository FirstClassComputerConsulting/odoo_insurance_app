# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.fields import Datetime
from odoo.exceptions import Warning
from random import randint
from freezegun import freeze_time
from datetime import date, datetime, timedelta
from time import time, localtime, gmtime, strftime,sleep
import time
import threading
import pytz
import ctypes
 
class OdooDateTime(Datetime):
    _inherit = "fields.Date"
    _name = "fields.Date"
    @staticmethod
    def now(*args):
        """Return the current day and time in the format expected by the ORM.

        .. note:: This function may be used to compute default values.
        """
        print("===================This will be nice to see!")
        # microseconds must be annihilated as they don't comply with the server datetime format
        return datetime.now().replace(microsecond=0)


class odootycoon_respartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    unlockcost = fields.Float('Unlock Cost', default=750)
    unlocked = fields.Boolean('Unlocked', default=False)
    
    
        
    def unlockcustomer(self):
        for res in self:
            gamemanager = res.env['odootycoon.gamemanager'].search([('name', '=', 'New Game')])

            if gamemanager.cash >= res.unlockcost:
                res.unlocked = True
                gamemanager.cash -= res.unlockcost
            else:
                raise Warning('You do not have enough money to unlock the %s customer' % res.name)
        return 0

    def customMethod(self):
        print("Custom Method called")
        return True
class odootycoon_salesorder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    state = fields.Selection([
        ('draft', 'Draft Order'),
        ('verify', 'Verify Order'),
        ('sale', 'Cooking'),
        ('quality', 'Quality Check'),
         ('outdelivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def VerifyOrder(self):
        for rec in self:
            rec.state = 'verify'
        return True



        
class odootycoon_producttemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    unlockcost = fields.Float('Unlock Cost', default=750)
    unlocked = fields.Boolean('Unlocked', default= False)
    level = fields.Integer('Level',default=1)


    def unlockproduct(self):
        print("Unlock Product")
        gamemanager = self.env['odootycoon.gamemanager'].search([('name', '=', 'New Game')])
        print(gamemanager)
        if gamemanager.cash >= self.unlockcost:
            self.unlocked = True
            gamemanager.cash -= self.unlockcost
        else:
            raise Warning('You do not have enough money to unlock the %s product' % self.name)

stop_threads = False
 
class gameThread (threading.Thread):
        def __init__(self, threadID, name,  counter, day):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.day = day
        def run(self):
            print ("Starting " + self.name)
            # Get lock to synchronize threads
            gameThread.set_time(self.name, 10, self.counter,self.day)
            # Free lock to release next thread  
         
        @staticmethod
        def set_time(threadName, delay,counter,day):
            
            s = '2020/01/01'
            date = datetime.strptime(s, "%Y/%m/%d")
            while counter:
                global stop_threads
                if stop_threads:
                    break
                modified_date = date +  timedelta(days=day)
                freezer = freeze_time(modified_date )
                freezer.start()
                
                sleep(delay)
                print ("%s: %s - %s" % (threadName, time.ctime(time.time()),counter))
                day = day + 1 
                counter -= 1

class odootycoon_gamemanager(models.Model):
    _name = 'odootycoon.gamemanager'
    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current Day", default=1)
    cash = fields.Float("Cash", default=1000)
    
     

    def checktime(self):
        
        global stop_threads
        stop_threads = False
        # Create new threads
        thread1 = gameThread(1, "Thread-1", 100,self.day)
        thread1.start()
        # Add threads to thread list
        #self.threads.append(thread1)
 

        # Wait for all threads to complete
        #for t in threads:
        #    t.join()

    def killthread(self):
        global stop_threads
        stop_threads = True

    def nextday(self):
        for o in self:
             
            # Process Unlocked Products
            products = o.env['product.template'].search([('unlocked','=', True)])

            cash = 0
            for product in products:
                numsold = randint(5,25)
                print (numsold)
                cash += product.list_price * numsold

            # Process Unlocked Customers
            customers = o.env['res.partner'].search([('unlocked', '=', True)])


            for customer in customers:

                cash *= 1.06 # 6% bonus for every customer we unlock


            o.write({'day': o.day + 1 ,'cash': o.cash + cash})
            return True
    def skip5days(self):
        for i in range(0,5):
            print(i)
            self.nextday()

    def skip30days(self):
        for i in range(0,30):
            print(i)
            self.nextday()
    def resetgame(self):
        self.day = 1
        self.cash = 1000
        self.env['product.template'].search([('unlocked', '=', True)]).write({'unlocked': False})







