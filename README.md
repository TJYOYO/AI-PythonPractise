# PythonPractise

一个综合性的Python机器学习练习项目，涵盖了从基础Python语法到高级深度学习应用的多个方面。

## 项目概述

本项目是一个Python学习和实践项目，主要用于：
- 学习Python编程基础（类、对象、实例字段与类字段等）
- 实践PyTorch深度学习框架
- 探索Hugging Face transformers库的各种应用
- 实现完整的机器学习工作流程（数据预处理、模型训练、评估、推理）

## 项目结构

```
AI-PythonPractise/
├── 根目录文件
│   ├── data_preprocessing.py      # 图像数据预处理（使用PyTorch和torchvision）
│   ├── FaceRecognition.py         # 人脸识别模型加载（使用MobileNetV2）
│   ├── FineTuning.py              # 模型微调训练
│   ├── Inference.py               # 模型推理
│   ├── Save.py                    # 模型保存
│   ├── Verify.py                  # 模型验证和准确率计算
│   ├── Test_instance_class_fields.py  # Python类字段测试（实例字段 vs 类字段）
│   ├── LICENSE                    # MIT许可证
│   ├── README.md                  # 项目说明文档
│   └── .gitignore                 # Git忽略配置
├── main/                          # 主模块目录
│   ├── data_preprocessing.py      # 数据预处理
│   ├── Datasets.py                # 数据集下载（使用kagglehub下载LFW数据集）
│   ├── inference.py               # 推理
│   ├── model_evaluation.py        # 模型评估
│   ├── model_training.py          # 模型训练
│   └── save_model.py              # 模型保存
└── testHuggingFace/               # Hugging Face测试目录
    ├── Question-Answering.py      # 问答系统测试
    ├── sentiment-analysis.py      # 情感分析测试
    ├── TextGeneration.py          # 文本生成测试（使用GPT-2）
    ├── Translate.py               # 机器翻译测试（英译中）
    └── Tokenizers/
        └── UsingModelsAndTokenizersInstandPipeline.py  # Tokenizer和模型使用
```

## 技术栈

### 深度学习框架
- **PyTorch**: 用于模型训练、微调和推理
- **torchvision**: 用于图像数据处理和增强

### Hugging Face生态系统
- **transformers**: 用于各种NLP任务（文本生成、问答、情感分析、翻译）
- **预训练模型**: 
  - GPT-2 (文本生成)
  - DistilBERT (情感分析)
  - MobileNetV2 (图像分类)
  - opus-mt-en-zh (英译中翻译)

### 数据处理
- **PIL/Pillow**: 图像处理
- **datasets**: 数据集加载
- **kagglehub**: 数据集下载（LFW人脸数据集）

### 其他工具
- **Python 3.x**: 主要编程语言
- **Git**: 版本控制

## 安装和依赖

### 环境要求
- Python 3.7+
- pip 或 conda

### 安装步骤

1. 克隆项目：
```bash
git clone https://github.com/TJYOYO/PythonPractise.git
cd PythonPractise
```

2. 创建虚拟环境（推荐）：
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. 安装依赖：
```bash
pip install torch torchvision transformers datasets pillow kagglehub
```

## 功能模块说明

### 1. 人脸识别系统
位于项目根目录，展示了完整的端到端机器学习工作流程：

1. **数据预处理** (`data_preprocessing.py`): 加载和预处理图像数据
2. **模型加载** (`FaceRecognition.py`): 加载预训练的MobileNetV2模型
3. **微调训练** (`FineTuning.py`): 在自定义数据集上微调模型
4. **模型验证** (`Verify.py`): 计算模型在测试集上的准确率
5. **模型保存** (`Save.py`): 保存微调后的模型
6. **模型推理** (`Inference.py`): 使用训练好的模型进行预测

### 2. Hugging Face测试
位于`testHuggingFace/`目录，展示了transformers库的各种应用：

- **文本生成** (`TextGeneration.py`): 使用GPT-2生成文本
- **问答系统** (`Question-Answering.py`): 基于上下文的问答
- **情感分析** (`sentiment-analysis.py`): 分析文本情感（正面/负面）
- **机器翻译** (`Translate.py`): 英译中翻译
- **Tokenizer使用** (`Tokenizers/`): 手动使用tokenizer和模型

### 3. Python基础练习
- **类字段测试** (`Test_instance_class_fields.py`): 演示Python中实例字段和类字段的区别

### 4. 主模块
位于`main/`目录，包含更模块化的实现：
- 数据集下载和管理
- 模型训练和评估的分离
- 可重用的组件

## 使用方法

### 运行人脸识别示例
1. 准备图像数据集，按类别组织在文件夹中
2. 更新`data_preprocessing.py`中的路径：
```python
train_dataset = datasets.ImageFolder(root='path_to_train_data', transform=transform)
test_dataset = datasets.ImageFolder(root='path_to_test_data', transform=transform)
```
3. 按顺序运行脚本：
```bash
python data_preprocessing.py
python FaceRecognition.py
python FineTuning.py
python Verify.py
python Save.py
python Inference.py
```

### 运行Hugging Face示例
```bash
# 文本生成
python testHuggingFace/TextGeneration.py

# 情感分析
python testHuggingFace/sentiment-analysis.py

# 问答系统
python testHuggingFace/Question-Answering.py

# 机器翻译
python testHuggingFace/Translate.py
```

### 运行Python基础示例
```bash
python Test_instance_class_fields.py
```

## 注意事项

1. **数据路径**: 部分脚本中的路径是占位符，需要根据实际情况修改
2. **硬件要求**: 深度学习模型训练需要GPU支持以获得更好的性能
3. **依赖版本**: 建议使用较新版本的PyTorch和transformers库
4. **数据集**: LFW数据集下载需要kaggle账号和API token

## 许可证

本项目基于MIT许可证开源 - 查看[LICENSE](LICENSE)文件了解详情。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 作者

- TJYOYO

## 致谢

- 感谢Hugging Face团队提供的优秀transformers库
- 感谢PyTorch社区
- 感谢所有开源项目的贡献者

---

*本项目主要用于学习和研究目的，适合作为机器学习入门和实践的参考项目。*
