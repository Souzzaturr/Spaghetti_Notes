import hashlib

def dar_hash(senha: str) -> str:
    senha_bytes = senha.encode()
    hash_senha_bytes = hashlib.sha256(senha_bytes)
    hash_senha = hash_senha_bytes.hexdigest(hash_senha_bytes)

    return hash_senha

#---

