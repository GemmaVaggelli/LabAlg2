from AlberoBinario import ABR
from AlberoRossoNero import ARN


def main():
    tree = ABR()
    for i in range(10, 0, -1):
        tree.insert(i)
        print(i)

    print("ABR: ")
    tree.inorder()

    treeRN = ARN()
    treeRN.insert(10)
    treeRN.insert(11)
    treeRN.insert(12)

    print("ARN: ")
    treeRN.inorderRN(treeRN.root)


if __name__ == "__main__":
    main()
