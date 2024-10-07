from typing_extensions import List
from .ctypes import loader
import ctypes

class MakTub:

    def __init__(self,seed:str) -> None:
        self.c_object = loader.newMakTub(
            "%s".encode("utf-8"),
            seed.encode("utf-8")
        )

    def set_seed(self,seed:str):
        loader.MakTub_set_seed(
            self.c_object,
            "%s".encode("utf-8"),
            seed.encode("utf-8")
        )


    def aply_seed_modification(self,positions:List[int],valid_chars:str):
        positions_size = len(positions)
        array = (ctypes.c_int * positions_size)()
        for i in range(positions_size):
            array[i] = int(positions[i])

        loader.MakTub_aply_seed_modification(
            self.c_object,
            array,
            positions_size,
            valid_chars.encode("utf-8")
        )


    def __str__(self) -> str:
        return self.get_seed()




    def get_seed(self):
        return loader.MakTub_get_seed(self.c_object).decode()



    def generate_num(self,start:int,end:int):
        return loader.Maktub_generate_num(self.c_object,start,end)



    def __del__(self):
        loader.MakTub_free(self.c_object)
