from bson import ObjectId


class Produto():
    
    
    def __init__(self, name, quantity, price, _id=None):
        self._id = ObjectId(_id)
        self.name = name
        self.quantity = quantity
        self.price = price
        
        
    def to_dict(self):
        produto_dict = {
            "_id": self._id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }
        
        if self._id:
            produto_dict['_id'] = self._id
        return produto_dict