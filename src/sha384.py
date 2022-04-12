
class SHA384:
    def __init__(self):
        self.hashConstants = [
            0xcbbb9d5dc1059ed8, 0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939, 
            0x67332667ffc00b31, 0x8eb44a8768581511, 0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4 ]
        self.roundConstants = [
            0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
            0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
            0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
            0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
            0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
            0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
            0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
            0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
            0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
            0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
            0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
            0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
            0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
            0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
            0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
            0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
            0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
            0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
            0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
            0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817 ]
        
    def hash(self, raw_data):
        # 1. Pre-Process 'raw_data'
        data = [ord(char) for char in raw_data]

        data.append(128)

        while (len(data) % 128 != 0):
            data.append(0)
        
        schedule = ''.join([format(num, '08b') for num in data])

        if '1' in schedule[-128:]:
            schedule += format(8*len(raw_data), '01024b')
        else:
            schedule = schedule[:-128] + format(8*len(raw_data), '0128b')
        
        # 2. Chunk Loop
        blocks = []

        for x in range(0, len(schedule) // 1024):
            blocks.append([schedule[x*1024:(x*1024)+1024]])
            blocks[x] = [int(blocks[x][0][y:y+64], 2) for y in range(0, len(blocks[x][0]), 64)]
            blocks[x].extend([0]*64) 

        # 3. Compression Loop
        for block in range(0, len(blocks)):
            for entry in range(16, 80):
                s0 = (rotr(blocks[block][entry-15], 1)) ^ (rotr(blocks[block][entry-15], 8)) ^ (blocks[block][entry-15] >> 7)
                s1 = (rotr(blocks[block][entry-2], 19)) ^ (rotr(blocks[block][entry-2], 61)) ^ (blocks[block][entry-2]>> 6)
                blocks[block][entry] = (blocks[block][entry-16] + s0 + blocks[block][entry-7] + s1) % 2**64
    
        # 4. Mutation Loop
        for block in range(0, len(blocks)):
            a, b, c, d, e, f, g, h = self.hashConstants

            for entry in range(0, 80):
                s0 = (rotr(e, 14)) ^ (rotr(e, 18)) ^ (rotr(e, 41))
                ch = (e & f) ^ (~e & g)
                temp1 = (h + s0 + ch + self.roundConstants[entry] + blocks[block][entry]) % 2**64
                s1 = (rotr(a, 28)) ^ (rotr(a, 34)) ^ (rotr(a, 39))
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (s1 + maj) % 2**64

                h = g
                g = f
                f = e
                e = (d + temp1) % 2**64 
                d = c
                c = b
                b = a
                a = (temp1 + temp2) % 2**64 

            self.hashConstants[0] = (self.hashConstants[0] + a) % 2**64 
            self.hashConstants[1] = (self.hashConstants[1] + b) % 2**64 
            self.hashConstants[2] = (self.hashConstants[2] + c) % 2**64 
            self.hashConstants[3] = (self.hashConstants[3] + d) % 2**64 
            self.hashConstants[4] = (self.hashConstants[4] + e) % 2**64 
            self.hashConstants[5] = (self.hashConstants[5] + f) % 2**64
            self.hashConstants[6] = (self.hashConstants[6] + g) % 2**64
            self.hashConstants[7] = (self.hashConstants[7] + h) % 2**64 

        # 5. Digest Concatenation
        digest = ''.join([format(hash, '016x') for hash in self.hashConstants[:6]])

        return digest

# Right-Rotate Bitwise Operator. [exp. rotr('000111', 2) -> '110001']
def rotr(num, bits):
    return (num >> bits) | (num << (64 - bits))
