# 测试手册
## 快速开始
### 先决条件
请先进行配置并生成TEST.makefile
```bash
bash ./configure # 或 bash ./Configure
# 如果遇到问题，可以添加 -V 参数查看详细输出，具体参数参见 -H
```
### 执行
通过以下命令开始测试
```bash
cd ../../; make -f maintenance/tests/TEST.makefile all
```
## 配置选项（环境变量）
### DONT_UPDATE
* 类型：bool (0/1)
* 默认值：0
* 效果：开启则不会自动更新依赖
## 备忘录
### Configure 和 configure 两个脚本的差异
configure 是 Configure 的副本，但移除了复活节彩蛋且使用技术性的文本替换了幽默的文本