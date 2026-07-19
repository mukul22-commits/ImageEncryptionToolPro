from services.crypto.encryption_service import EncryptionService

result = EncryptionService.encrypt(

    "samples/samples.jpg",

    "output/test.enc",

    "Cyber@123"

)

print(result)