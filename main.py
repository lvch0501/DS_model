import re


def main():
    with open("data/raw/gwas_train_pos.txt", "r") as f:
        train_data = f.readlines()
        abstract = []
        for i in train_data:
            abstract.append(i.split("\t")[2])
        pattern1 = re.compile('rs[0-9]+')
        pattern2 = re.compile('[0-9]+[.]?[0-9]∗\s∗ [x|×]\s∗ [0-9]+ [\(]{0,1}−[0-9\s]+ [\)]{0,1}')
        pattern3 = re.compile('[0-9.] + [e|E][\(]{0,1}[0-9−] + [\)]{0,1}')
        pattern4 = re.compile(r'[0-9]+[.]?[0-9]*\s*[x|×]\s*[0-9]+[\(][-][0-9]+[\)]')
        #s = "P=3.7 x 10(-7)"
        #temp = re.findall(pattern4, s)
        #temp1 = re.findall(pattern3, s)
        count = 0
        clean = ''
        noise = ''
        for i in abstract:
            p_value = []
            snp = re.findall(pattern1, i)
            p_value = re.findall(pattern4, i)
            p_value.append(re.findall(pattern3, i))

            if len(snp)!=0:
                clean += i+"\n"
            else:
                noise += i+"\n"
            print()

        with open("data/new/new_with_snp.txt", 'w', encoding="utf-8") as code:
            code.write(clean)
        with open("data/new/new_not_with_snp.txt", 'w',encoding= "utf-8") as code:
            code.write(noise)
        print()
if __name__ == '__main__':
    main()