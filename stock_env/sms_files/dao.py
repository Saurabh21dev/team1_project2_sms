from database import db_session
import re
from models import Product,Stock,Supplier,Stransaction,Ctransaction,Corder,Sorder,Customer
#product table
class ProductDAO:
    @staticmethod
    def get_all_products():
        return db_session.query(Product).all()
       
    def get_product_by_id(Pid):
        return db_session.query(Product).filter(Product.Pid == Pid).first()

    @staticmethod
    def create_product(Pname, Description, Price):
        if any(arg is None for arg in [Pname, Description, Price]):
            return None
        
        if not re.match(r'^[A-Za-z\s]+$', Pname):
            return None
        
        if not re.match(r'^[A-Za-z\s]+$', Description):
            return None
        
        if Price <= 0:
            return None
        
        product = Product(Pname=Pname,Description=Description,Price=Price)
        db_session.add(product)
        db_session.commit()
        return product

    @staticmethod
    def update_product(Pid, Pname, Description, Price):
        if any(arg is None for arg in [Pname, Description, Price]):
            return None
        
        if not re.match(r'^[A-Za-z\s]+$', Pname):
            return None
        
        if not re.match(r'^[A-Za-z\s]+$', Description):
            return None
        
        if Price <= 0:
            return None
        
        product = db_session.query(Product).get(Pid)
        if product:
            product.Pname = Pname
            product.Description = Description
            product.Price = Price
            db_session.commit()
        return product

    @staticmethod
    def delete_product(Pid):
        product = db_session.query(Product).get(Pid)
        if product:
            db_session.delete(product)
            db_session.commit()
            return True
        return False

#supplier tables
class SupplierDAO:
    @staticmethod
    def get_all_suppliers():
        return db_session.query(Supplier).all()
       
    def get_supplier_by_id(Sid):
        return db_session.query(Supplier).filter(Supplier.Sid == Sid).first()

    @staticmethod
    def create_supplier(Sname, Scontact, Sadd):
        supplier = Supplier(Sname=Sname,Scontact=Scontact,Sadd=Sadd)
        db_session.add(supplier)
        db_session.commit()
        return supplier

    @staticmethod
    def update_supplier(Sid, Sname, Scontact, Sadd):
        supplier = db_session.query(Supplier).get(Sid)
        if supplier:
            supplier.Sname = Sname
            supplier.Scontact = Scontact
            supplier.Sadd = Sadd
            db_session.commit()
        return supplier

    @staticmethod
    def delete_supplier(Sid):
        supplier = db_session.query(Supplier).get(Sid)
        if supplier:
            db_session.delete(supplier)
            db_session.commit()
            return True
        return False

#customer tables
class CustomerDAO:
    @staticmethod
    def get_all_customers():
        return db_session.query(Customer).all()
       
    def get_customer_by_id(Cid):
        return db_session.query(Customer).filter(Customer.Cid == Cid).first()

    @staticmethod
    def create_customer(Cname, Ccontact, Cadd):
        customer = Customer(Cname=Cname,Ccontact=Ccontact,Cadd=Cadd)
        db_session.add(customer)
        db_session.commit()
        return customer

    @staticmethod
    def update_customer(Cid, Cname, Ccontact, Cadd):
        customer = db_session.query(Customer).get(Cid)
        if customer:
            customer.Cname = Cname
            customer.Ccontact = Ccontact
            customer.Cadd = Cadd
            db_session.commit()
        return customer

    @staticmethod
    def delete_customer(Cid):
        customer = db_session.query(Customer).get(Cid)
        if customer:
            db_session.delete(customer)
            db_session.commit()
            return True
        return False

#stocks table    
class StockDAO:
    @staticmethod
    def get_all_stocks():
        return db_session.query(Stock).all()
    

    def get_stock_by_id(Sid):
        return db_session.query(Stock).filter(Stock.Sid == Sid).first()

    

    @staticmethod
    def create_stock(Pid, Qnt):
        stock = Stock(Pid=Pid,Qnt=Qnt)
        db_session.add(stock)
        db_session.commit()
        return stock

    @staticmethod
    def update_stock(Sid, Pid, Qnt):
        stock = db_session.query(Stock).get(Sid)
        if stock:
            stock.Sid= Sid
            stock.Pid = Pid
            stock.Qnt = Qnt
            db_session.commit()
        return stock

    @staticmethod
    def delete_stock(Sid):
        stock = db_session.query(Stock).get(Sid)
        if stock:
            db_session.delete(stock)
            db_session.commit()
            return True
        return False
    
#Stock Order table
class SorderDAO:
    @staticmethod
    def get_all_sorders():
        return db_session.query(Sorder).all()
    
    def get_sorder_by_id(Oid):
        return db_session.query(Sorder).filter(Sorder.Oid == Oid).first()

    

    @staticmethod
    def create_sorder(Sid, Pid, Pqnt):
        sorder = Sorder(Sid=Sid,Pid=Pid,Pqnt=Pqnt)
        db_session.add(sorder)
        db_session.commit()
        return sorder

    @staticmethod
    def update_sorder(Oid,Pid, Sid, Pqnt):
        sorder = db_session.query(Sorder).get(Oid)
        if sorder:
            sorder.Oid=Oid
            sorder.Pid = Pid
            sorder.Sid = Sid
            sorder.Pqnt = Pqnt
            db_session.commit()
        return sorder

    @staticmethod
    def delete_sorder(Oid):
        sorder = db_session.query(Sorder).get(Oid)
        if sorder:
            db_session.delete(sorder)
            db_session.commit()
            return True
        return False
    
#customer order table    
class CorderDAO:
    @staticmethod
    def get_all_corders():
        return db_session.query(Corder).all()
    
    def get_corder_by_id(Oid):
        return db_session.query(Corder).filter(Corder.Oid == Oid).first()
    
    

    @staticmethod
    def create_corder(Cid, Pid, Pqnt):
        corder = Corder(Cid=Cid,Pid=Pid,Pqnt=Pqnt)
        db_session.add(corder)
        db_session.commit()
        return corder

    @staticmethod
    def update_corder(Oid,Pid, Cid, Pqnt):
        corder = db_session.query(Corder).get(Oid)
        if corder:
            corder.Oid=Oid
            corder.Pid = Pid
            corder.Cid = Cid
            corder.Pqnt = Pqnt
            db_session.commit()
        return corder

    @staticmethod
    def delete_corder(Oid):
        corder = db_session.query(Corder).get(Oid)
        if corder:
            db_session.delete(corder)
            db_session.commit()
            return True
        return False

#Supplier transcation table
class StransactionDAO:
    @staticmethod
    def get_all_stransactions():
        return db_session.query(Stransaction).all()
    

    def get_stransactions_by_id(Tid):
        return db_session.query(Stransaction).filter(Stransaction.Tid == Tid).first()
    

    @staticmethod
    def create_stransaction(Oid,TDate, Tprice):
        transaction = Stransaction(Oid=Oid,TDate=TDate,Tprice=Tprice)
        db_session.add(transaction)
        db_session.commit()
        return transaction

    @staticmethod
    def update_stransaction(Tid, Oid, TDate,Tprice):
        transaction = db_session.query(Stransaction).get(Tid)
        if transaction:
            transaction.Oid = Oid
            transaction.TDate = TDate
            transaction.Tprice = Tprice         
            db_session.commit()
        return transaction

    @staticmethod
    def delete_stransaction(Tid):
        transaction = db_session.query(Stransaction).get(Tid)
        if transaction:
            db_session.delete(transaction)
            db_session.commit()
            return True
        return False
    
#Customer transctions table
class CtransactionDAO:
    @staticmethod
    def get_all_ctransactions():
        return db_session.query(Ctransaction).all()
    
    def get_ctransactions_by_id(Tid):
        return db_session.query(Ctransaction).filter(Ctransaction.Tid == Tid).first()
    

    @staticmethod
    def create_ctransaction(Oid,TDate, Tprice):
        transaction = Ctransaction(Oid=Oid,TDate=TDate,Tprice=Tprice)
        db_session.add(transaction)
        db_session.commit()
        return transaction

    @staticmethod
    def update_ctransaction(Tid, Oid, TDate,Tprice):
        transaction = db_session.query(Ctransaction).get(Tid)
        if transaction:
            transaction.Oid = Oid
            transaction.TDate = TDate
            transaction.Tprice = Tprice         
            db_session.commit()
        return transaction

    @staticmethod
    def delete_ctransaction(Tid):
        transaction = db_session.query(Ctransaction).get(Tid)
        if transaction:
            db_session.delete(transaction)
            db_session.commit()
            return True
        return False