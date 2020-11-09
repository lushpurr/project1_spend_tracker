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

merchant1 = Merchant('BP', True)
merchant_repository.save(merchant1)

merchant2 = Merchant('Wetherspoons', True)
merchant_repository.save(merchant2)

tag1 = Tag('Fuel', True)
tag_repository.save(tag1)

tag2 = Tag('Food', True)
tag_repository.save(tag2)

transaction1 = Transaction(10.00, merchant1, tag1)
transaction_repository.save(transaction1)

transaction2 = Transaction(30.00, merchant2, tag2)
transaction_repository.save(transaction2)
pdb.set_trace()