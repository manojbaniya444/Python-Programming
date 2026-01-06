from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
  @abstractmethod
  def pay(self, amount: int):
    pass
  
# old payment service that we want to support (assume the service is third party with pay_old method)
class OldPaymentService:
  def pay_old(amount: int):
    print(f"Paying the amount {amount} using the old payment method")
    
# our other payment processor
class StripePaymentService(PaymentProcessor):
  def pay(self, amount: int):
    print(f"Paying the amount {amount} using the stripe payment service")
    
class SomeOtherPaymentSerice(PaymentProcessor):
  def pay(self, amount: int):
    print(f"Paying the amount {amount} using some other popular modern processor")
    


# the logic we use in the service
def process_payment(payment_processor: PaymentProcessor, amount: int):
  payment_processor.pay(amount)
    
# In the process_payment we send our payment service that we define with the interface PaymentProcessor easily but it do not accept the OldPayementService
# In that we make adapter so that it accept in the process_payment
# For that we make a class that implement the PaymentProcessor

class OldPaymentAdapter(PaymentProcessor):
  def __init__(self, old_payment_service: OldPaymentService):
    self.old_payment_service = old_payment_service
    
  def pay(self, amount: int):
    self.old_payment_service.pay_old(amount)
    
old_payment_service = OldPaymentAdapter(OldPaymentService)
process_payment(old_payment_service, 100)

# or

stripe_payment_service = StripePaymentService()
process_payment(stripe_payment_service, 660)