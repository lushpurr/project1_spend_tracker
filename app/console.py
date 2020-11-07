import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()

merchant1 = Merchant('BP')
merchant_repository.save(merchant1)

tag1 = Tag('Fuel')
tag_repository.save(tag1)

transaction1 = Transaction(10.00, merchant1, tag1)
transaction_repository.save(transaction1)

pdb.set_trace()