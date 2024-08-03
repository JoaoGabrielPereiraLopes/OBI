tamanho=int(input())
pos_disk=int(input())
pos_plane=int(input())
if pos_plane>pos_disk:
    print(tamanho-pos_plane+pos_disk)
else:
    print(pos_disk-pos_plane)