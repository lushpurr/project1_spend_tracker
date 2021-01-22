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

merchant2 = Merchant('Amazon', True)
merchant_repository.save(merchant2)

merchant3 = Merchant('Wetherspoons', False)
merchant_repository.save(merchant3)

merchant4 = Merchant('Dr Evil', True)
merchant_repository.save(merchant4)

tag1 = Tag('Fuel', True)
tag_repository.save(tag1)

tag2 = Tag('Food', True)
tag_repository.save(tag2)

tag3 = Tag('Book', True)
tag_repository.save(tag3)

tag4 = Tag('Destroy the world', True)
tag_repository.save(tag4)

transaction1 = Transaction(10.00, merchant1, tag1)
transaction_repository.save(transaction1)

transaction2 = Transaction(30.00, merchant2, tag2)
transaction_repository.save(transaction2)

transaction4 = Transaction(1000000.00, merchant4, tag4)
transaction_repository.save(transaction4)

pdb.set_trace()