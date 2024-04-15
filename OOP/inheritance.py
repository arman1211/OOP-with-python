class Vehice:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
    def __repr__(self,model) -> str:
        return f' this is {self.name} and its price is {self.price}. the model is{model}'

class Bus(Vehice):
    def __init__(self, name, price,model) -> None:
        self.model = model
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__(self.model)

class ACbus(Bus):
    def __init__(self, name, price, model,temp) -> None:
        self.temp = temp
        super().__init__(name, price, model)
    def __repr__(self) -> str:
        
        print(f'temp is {self.temp}')
        return super().__repr__()
    

ena = ACbus('ena',20000,'ena-bpd22',30)

print(ena)