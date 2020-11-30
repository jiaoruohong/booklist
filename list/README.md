# Book List

## 编译

```bash
python3 ./genInputs.py
latex -pdflatex=xelatex -pdf ./note_cn.tex
```

## 格式要求

- 书籍信息填写在 **./parts** 文件夹下
- 文件名格式： **书名-语言-作者.tex** <br/>
  **只能出现中英字符和数字，其余标点符号和空格一律用“-”代替** <br/>
  **英文人名一律用英文表示，中日韩人名用中文表示** <br/>
  **语言只有两种（en：标准英文，cn：简体中文）** <br/>
  文件名中只编辑一作
- 书籍信息分四部分： **标题、作者、出版商和语言** <br/>
  作者栏不用写译者，但要记录全部原始作者
  ```bash
  Title &
  Author &
  Publisher &
  cn or en \\ \hline
  ```

