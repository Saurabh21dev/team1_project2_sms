from decimal import Decimal
import datetime
import strawberry
from typing import List
from dao import ProductDAO,StockDAO,SorderDAO,StransactionDAO,SupplierDAO,CorderDAO,CustomerDAO,CtransactionDAO


@strawberry.type
class ProductType:
    Pid: int
    Pname: str
    Description: str
    Price: Decimal

@strawberry.type
class SupplierType:
    Sid:int
    Sname:str
    Scontact:int
    Sadd:str

@strawberry.type
class CustomerType:
    Cid:int
    Cname:str
    Ccontact:int
    Cadd:str

@strawberry.type
class StockType:
    Stid:int
    Pid: int
    Qnt: int
    
@strawberry.type
class CorderType:
    Oid:int
    Cid:int
    Pid: int
    Pqnt: int
    
@strawberry.type
class SorderType:
    Oid:int
    Sid:int
    Pid: int
    Pqnt: int


@strawberry.type
class StransactionType:
    Tid:int
    Oid: int
    TDate: datetime.datetime
    Tprice: Decimal

@strawberry.type
class CtransactionType:
    Tid:int
    Oid: int
    TDate: datetime.datetime
    Tprice: Decimal

try:
    @strawberry.type
    class Query:
        @strawberry.field
        def getProducts(self) -> List[ProductType]:
            return ProductDAO.get_all_products()
        
        @strawberry.field
        def getProductById(self,Pid:int) -> ProductType:
            return ProductDAO.get_product_by_id(Pid)
        
        @strawberry.field
        def getSuppliers(self) -> List[SupplierType]:
            return SupplierDAO.get_all_suppliers()
        

        @strawberry.field
        def getSupplierById(self,Sid:int) -> SupplierType:
            return SupplierDAO.get_supplier_by_id(Sid)
        
        @strawberry.field
        def getCustomers(self) -> List[CustomerType]:
            return CustomerDAO.get_all_customers()
        
        @strawberry.field
        def getCustomerById(self,Cid:int) -> CustomerType:
            return CustomerDAO.get_customer_by_id(Cid)

        @strawberry.field
        def getStocks(self) -> List[StockType]:
            return StockDAO.get_all_stocks()
        
        @strawberry.field
        def getStockById(self,Stid:int) -> StockType:
            return StockDAO.get_stocks_by_id(Stid)
        
        @strawberry.field
        def getCOrders(self) -> List[CorderType]:
            return CorderDAO.get_all_corders()
        

        @strawberry.field
        def getCOrderById(self,Oid:int) -> CorderType:
            return CorderDAO.get_corder_by_id(Oid)
        
        @strawberry.field
        def getSOrders(self) -> List[SorderType]:
            return SorderDAO.get_all_sorders()
    

        @strawberry.field
        def getSOrderById(self,Oid:int) ->SorderType:
            return SorderDAO.get_sorder_by_id(Oid)
        
        #for transactions table
        @strawberry.field
        def getCTransactions(self) -> List[CtransactionType]:
            return CtransactionDAO.get_all_ctransactions()
        
        @strawberry.field
        def getCtransctionById(self,Tid:int) -> CtransactionType:
            return CtransactionDAO.get_ctransactions_by_id(Tid)
        

        
        @strawberry.field
        def getSTransactions(self) -> List[StransactionType]:
            return StransactionDAO.get_all_stransactions()
        
        @strawberry.field
        def getStransctionById(self,Tid:int) -> StransactionType:
            return StransactionDAO.get_stransactions_by_id(Tid)
        


except Exception as e:
    print("An error happens in query type")


@strawberry.type
class Mutation:
    #products table
    @strawberry.mutation
    def createProduct(self, Pname: str, Description: str,Price: Decimal) -> ProductType:
        return ProductDAO.create_product(Pname, Description,Price)

    @strawberry.mutation
    def updateProduct(self, Pid:int,Pname: str, Description: str,Price: Decimal) -> ProductType:
        return ProductDAO.update_product(Pid,Pname, Description, Price)
    
    @strawberry.mutation
    def deleteProduct(self, Pid: int) -> bool:
        success = ProductDAO.delete_product(Pid)
        return success
    
    #Stocks table
    @strawberry.mutation
    def createStock(self,Pid:int, Qnt: int) -> StockType:
        return StockDAO.create_stock(Pid, Qnt)
    
    @strawberry.mutation
    def updateStock(self,Stid:int, Pid: int, Qnt: int) -> StockType:
        return StockDAO.update_stock(Stid,Pid, Qnt)
    
    @strawberry.mutation
    def deleteStock(self, Stid: int) -> bool:
        success = StockDAO.delete_stock(Stid)
        return success
    
    #SOrders table 
    @strawberry.mutation
    def createSOrder(self,Sid: int, Pid: int,Pqnt: int) -> SorderType:
        return SorderDAO.create_sorder(Sid,Pid,Pqnt)
    
    @strawberry.mutation
    def updateSOrder(self,Oid: int, Sid: int, Pid: int,Pqnt: int) -> SorderType:
        return SorderDAO.update_sorder(Oid,Sid,Pid,Pqnt)
    
    @strawberry.mutation
    def deleteSOrder(self, Oid: int) -> bool:
        success = SorderDAO.delete_sorder(Oid)
        return success
    
     #TOrders table  
    @strawberry.mutation
    def createCOrder(self,Cid: int, Pid: int,Pqnt: int) -> CorderType:
        return CorderDAO.create_corder(Cid,Pid,Pqnt)
    
    @strawberry.mutation
    def updateCOrder(self,Oid: int, Cid: int, Pid: int,Pqnt: int) -> CorderType:
        return CorderDAO.update_corder(Oid,Cid,Pid,Pqnt)
    
    @strawberry.mutation
    def deleteCOrder(self, Oid: int) -> bool:
        success = CorderDAO.delete_corder(Oid)
        return success
    
    #STransaction table 
    @strawberry.mutation
    def createSTransaction(self,Oid: int,TDate: datetime.datetime,Tprice:Decimal) -> StransactionType:
        return StransactionDAO.create_stransaction(Oid,TDate,Tprice)
    
    @strawberry.mutation
    def updateSTransaction(self,Tid:int,Oid: int,TDate: datetime.datetime,Tprice:Decimal) -> StransactionType:
        return StransactionDAO.update_stransactione(Tid,Oid,TDate,Tprice)

    @strawberry.mutation
    def deleteSTransaction(self, Tid: int) -> bool:
        success = StransactionDAO.delete_stransaction(Tid)
        return success
    
    #CTransaction table ""
    @strawberry.mutation
    def createCTransaction(self,Oid: int,TDate: datetime.datetime,Tprice:Decimal) -> CtransactionType:
        return CtransactionDAO.create_ctransaction(Oid,TDate,Tprice)
    
    @strawberry.mutation
    def updateCTransaction(self,Tid:int,Oid: int,TDate: datetime.datetime,Tprice:Decimal) -> CtransactionType:
        return CtransactionDAO.update_ctransaction(Tid,Oid,TDate,Tprice)

    @strawberry.mutation
    def deleteCTransaction(self, Tid: int) -> bool:
        success = CtransactionDAO.delete_ctransaction(Tid)
        return success
    
    #supplier Table 

    @strawberry.mutation
    def createSupplier(self,Sname: str,Scontact: int,Sadd:str) -> SupplierType:
        return SupplierDAO.create_supplier(Sname,Scontact,Sadd)

    @strawberry.mutation
    def updateSupplier(self, Sid: int, Sname: str,Scontact: int,Sadd:str) -> SupplierType:
        return SupplierDAO.update_supplier(Sid, Sname,Scontact,Sadd)
    
    @strawberry.mutation
    def deleteSupplier(self, Sid: int) -> bool:
        success = SupplierDAO.delete_supplier(Sid)
        return success
    
    #Customer table
    @strawberry.mutation
    def createCustomer(self, Cname: str,Ccontact: int,Cadd:str) -> CustomerType:
        return CustomerDAO.create_customer(Cname,Ccontact,Cadd)

    @strawberry.mutation
    def updateCustomer(self, Cid: int, Cname: str,Ccontact: int,Cadd:str) -> CustomerType:
        return CustomerDAO.update_customer(Cid,Cname,Ccontact,Cadd)
    
    @strawberry.mutation
    def deleteCustomer(self, Cid: int) -> bool:
        success = CustomerDAO.delete_customer(Cid)
        return success

    

# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)