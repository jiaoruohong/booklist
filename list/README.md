# Book List

## 字体要求

- [Source Han Sans (SC)](https://github.com/adobe-fonts/source-han-sans)
- [Source Han Serif (CN)](https://github.com/adobe-fonts/source-han-serif)

## 编译

```bash
python3 ./genInputs.py
latexmk -pdflatex=xelatex -pdf ./BookList.tex
```

## 格式要求

- 书籍信息填写在 `./part` 文件夹下
- 文件名格式： **书名-语言-作者-出版年份-资料有无.tex** <br/>
  **只能出现中英字符和数字，其余标点符号和空格一律用“-”代替** <br/>
  **英文人名一律用英文表示，中日韩人名用中文表示** <br/>
  **语言只有两种（EN：标准英文，CN：简体中文）** <br/>
  **CD等各种资料有无（Y：yes，N：no）** <br/>
  **文件名中只编辑一作**
- 书籍信息分6部分： **标题、作者、出版商、出版年份、是否含有资料（CD等随书资料）和语言** <br/>
  **作者栏不用写译者，但要记录全部原始作者（不超过5人）**
  ```bash
  Title &
  Author &
  Publisher &
  Publish Year &
  Has data or not (Y/N) &
  CN or EN \\ \hline
  ```

