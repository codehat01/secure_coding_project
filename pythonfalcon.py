import falcon_post_crypto

public_key, secret_key = falcon_post_crypto.generate_keys_py()
public_key = bytes(public_key)
secret_key = bytes(secret_key)
message = input("Enter the message to sign: ").encode()
signed_message = falcon_post_crypto.sign_message_py(message, secret_key)
signed_message = bytes(signed_message)
verification_message = input("Enter the message to verify: ").encode()

verified_message = falcon_post_crypto.verify_message_py(signed_message, public_key)
print("Signed message (bytes):", signed_message)
print("Verified message (bytes):", verified_message)
print("Verification input message (bytes):", verification_message)

verified_message_bytes = bytes(verified_message)

if verified_message_bytes == verification_message:
    print("Signature verified successfully!")
else:
    print("Verification failed. The message does not match!")

print("Verified message (bytes):", verified_message_bytes)
print("Verification input message (bytes):", verification_message)
