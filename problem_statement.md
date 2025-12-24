# Problem Statement

Understanding source code is a major challenge for beginners in programming.
Many codebases lack clear comments, and existing comments often focus on
implementation details rather than explaining intent.

In addition, compiler and runtime error messages are typically technical and
difficult for non-experts to interpret. This creates a steep learning curve
and slows down the learning process.

With the increasing availability of Transformer-based language models, there
is an opportunity to automatically generate readable code comments.
However, it is not well understood how different model choices—such as
pre-trained models versus models trained from scratch—perform under
limited data conditions.

This project investigates the following questions:
- Can Transformer-based models generate meaningful code comments?
- How does a pre-trained model compare to a from-scratch model?
- What limitations arise when training data is extremely limited?

The goal is not to build a production-ready system, but to analyze model
behavior, limitations, and learning outcomes in a controlled experimental
setting.
