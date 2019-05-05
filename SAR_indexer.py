#!/usr/bin/python3

'''
Proyecto de Prácticas SAR: indexer
Autores:
Omar Caja García
Zhihao Zhang
Pablo López Orrios
Jose Antonio Culla de Moya
'''

import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help = "News directory")
    parser.add_argument("index", help = "Index name")

    