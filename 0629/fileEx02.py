#디렉토리 만드는법, 새파일 만드는법
# import os
# os.makedirs("C:/doit", exist_ok=True)
# f = open("C:/doit/새파일.txt", 'w')
# f.close()

# write_data.py
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()
