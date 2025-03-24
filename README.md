# SEMT20003: Introduction to AI
The course will introduce AI, with a focus on neural networks in PyTorch.

## Changelog
* Changes to the last part (Sec. 6 and onwards) of the LLM notes. 
* Clarified that the _code_ in the notebook in week 8 is non-examinable.  The statement at the top of that notebook now reads: "The code in this notebook is non-examinable!! We're doing some slightly weird stuff to get the nice visualisations!! Its the concepts illustrated in the notebook that are examinable!! i.e. only the stuff covered in the associated video is examinable."
* Added a note on extra exercises to this README.
* Added links to practice exams to this README.

## Staff
- [Laurence Aitchison](http://www.gatsby.ucl.ac.uk/~laurence/) [laurence.aitchison@bristol.ac.uk] (unit director)

## Teaching Block Structure
* This course runs in TB2.

## Prerequisites
Linear algebra, basic statistics, basic Python.

## Course Structure

The course is taught in a "flipped classroom model".  So there are no in-person lectures (we wouldn't be able to schedule them anyway given the wide range of cohorts on the course).  Instead, there are extensive pdf notes, iPython notebooks and videos.  There is a weekly 2-hour lab/problem class.  In that session, you can work on the question sheets and/or iPython notebooks, and ask TAs/me any questions on that material, or on any other part of the course. <!--, and the 1-hour weekly lecturer-led QA session (see Feedback below).-->


## Course Materials
Course materials for each week will be posted here on Monday.  Course materials each week will include some combination of:
* Notes
  - There are pdf notes for every week of taught material.
  - The notes are often long-ish, but that's only because I'm trying to be _thorough_ (e.g. I'm trying to include all the steps in derivations).  So the notes shouldn't in general be very dense.
  - The pdf notes will _usually, but not always_ include questions.
  - All questions will have worked answers.
* Notebooks
  - Each week, there will _usually, but not always_ be iPython notebooks, discussing practical aspects of training neural networks.
  - These iPython notebooks _occasionally_ have exercises.
  - The concepts in the iPython notebooks are examinable (see Exam section below for details on how code will be examined).
  - You don't learn code (well) by just reading.  Even if I haven't done exercises, open up your own Colab notebook alongside and type the code in to follow along.  Try the things that I'm doing.  Try something a bit different!
* Videos
  - There are always videos of me going through the pdf notes, and may sometimes be videos of me going through the iPython notebooks.
  - _Watching the videos isn't necessary!!!_  The videos just go through (slowly and thoroughly) the material in the underlying pdf notes / iPython notebook.  So if you read + understand the underlying notes / notebooks, the videos are not necessary.
  - To reiterate, the exam is based on the notes/notebooks, _not_ the videos.

## Synchronous sessions.
* Labs/problem classes 11am-1pm on Thursdays in QUEENS BLDG F.101a/b/c.  These start in week 1 (16th January):
  - TAs will be at all of these sessions.  I will be at most of the sessions.
  - In these sessions, you can work on the exercises in the pdf notes + CoLab notebooks for that week.
  - You can ask TAs/me about these exercises (or anything else in the course).
  - (Note that more "organised" material in this course is not really possible, as the course is taken so widely that some students have clashes with these sessions).
<!-- * Online, lecturer-led QA sessions, Thursday 4-5pm in TB1.  Held as a Teams meeting from the course Team.
  - Again, this is for feedback on all parts of the course, including lectures, notes, questions, iPython notebooks, past exams and the group coursework.
  - A couple of you will have clashes.  Apologies.  Timetabling have worked hard to minimize clashes, but it isn't actually possible to eliminate clashes, given the wide range of cohorts on the course.  The sessions will be recorded, and you can e.g. ask some else to submit your question.
  - Please do remind me if I forget to record! -->

## Why PyTorch
All the notebooks are going to be in [PyTorch](https://pytorch.org).  These days, you _need_ to know PyTorch if you're doing AI:
* PyTorch is currently the leading AI library, both for academic research, and industry.
* Fantastic docs + tutorials + libraries (better than any other library)
* Pythonic and hackable: you can look at + modify the source for just about anything
* PyTorch is great for learning AI, because it exposes alot of the underlying concepts, and doesn't hide them under abstractions.
* As we'll see, you can use PyTorch as GPU-enabled-numpy, so it is useful for many applications outside of traditional AI.

Other points:
* You won't need to install PyTorch.  All the iPython notebooks in the taught material are presented using [Google Colab](https://colab.research.google.com).

## Exam
* These exams are in the standard TB2 assessment period.
* The exam will be a 3 hour, 20 question, multiple choice, in-person exam.
* The exam is primarily based on the material in the pdf notes.
* But the material in the CoLab notebooks is examinable.  I may ask in-detail about the material in the first week's CoLab notebooks (as you can see from Q1 and Q2 of the sample exam).  For instance, you should know what `t.ones(2,3,4)` or `A.mean(2)` _does_ (along with the material in the GPU and intro to Python notebooks).  I won't ask questions that hinge on your knowledge of syntax, such as "how do you construct a tensor of zeros: `t.zeros(1)(2)` or `t.zeros(1.2)` or `t.zeros[[1],[2]]`.  But I might ask questions that hinge on your ability to read and interpret syntactically valid code.
* You aren't expected to know the material in the rest of the CoLab notebooks in that level of detail.  Specifically, the material in the rest of the CoLab notebooks may be examined in a couple of ways:
  - The CoLab notebooks can illustrate examinable concepts (e.g. Q7 and Q10 in the sample exam).
  - You may need to read more neural-network-y code, but where all information required would be clearly available in the code itself.  For instance, I could ask for a verbal description of the following neural network layer: `nn.Sequential(nn.Linear(in_features=100, out_features=200), nn.ReLU())`. I could give then several possible descriptions, with the correct description being: "A linear layer that takes vectors with 100 features and returns feature vectors with 200 features, followed by a relu nonlinearity".  But I wouldn't ask you to do that for `nn.Sequential(nn.Linear(100, 200), nn.ReLU())` as the code doesn't tell you what argument is `in_features` and which is `out_features`, and you really should to look it up to be sure.
* Things have changed quite alot since I took over the course, so the previous EMAT31530 exam is relevant, but nothing before that.
* The exam will focus on the _concepts_ rather than requiring you to learn specific math equations / PyTorch functions.
* [Instructions for MCQ exams](exams/OMR-student-intructions.pdf)
* The formula sheet in the sample exam is the same as that in the paper.
* I'm going to try hard to avoid needing memorisating equations in questions (see practice exams for details).

### Calculators in the exam

* The Methods of Artificial Intelligence Exam summer examination permits the use of a non-programmable calculator. We recommend the Casio FX-85 GT CW (solar-powered) or Casio FX-83GT CW (battery-powered).
* Please be advised that the use of a programmable calculator will be treated as an examination offence (and is likely to incur a penalty under the University Assessment Regulations). Your calculator will be visually checked by an invigilator during each exam.
* For students who do not own or are unable to obtain a non-programmable calculator prior to their exam, please contact the SEMT school office for further advice: semt-student-enquiries@bristol.ac.uk (e-mail enquiries) or Ada Lovelace Building room G1 (in-person enquiries; 9am-4pm Monday-Friday).
* If you are unsure whether your calculator is programmable or not, our recommendation is to use Google to search for your calculator model, and whether it is programmable or non-programmable. This usually provides a clear answer. Additionally, calculator brand websites often list this information under the product description for each model. If you are concerned and want someone to double check, the SEMT school office can offer support - see the contact details above.

### Practice exam!
Note that these previous exams are shorter (2 hour , 15 questions), whereas the exam this year is longer (3 hours , 20 questions).  The questions this year are exactly the same type and difficulty as the questions in previous years: the exam is just a bit longer.

[sample exam](exams/sample.pdf)

[sample exam answers](exams/sample_answers.pdf)

[23/24 exam](exams/2324.pdf)

[23/24 exam answers](exams/2324_answers.pdf)

## Understanding the capabilities of modern AI by it questions about the course

There are two problems:
* The course will introduce to the basics of how to train modern AI systems.  But it is also important for you to understand the capabilities of modern state-of-the-art AI systems.
* At the same time, you're going to have questions about the course material.  You can of course ask on the Teams, and in the TA-led problem classes.  But what if you want feedback immediately?

The solution is: try asking modern AI systems!  Specifically, for this kind of thing (programming, math deep learning), people reckon:
* [Gemini](https://gemini.google.com/app)
* [Claude](https://claude.ai)
* [Grok](https://grok.com)
* [DeepSeek](https://chat.deepseek.com)
* [ChatGPT](https://chatgpt.com) (But only o1, o3 etc, _not_ GPT-4o).

Are all pretty good.  There is a feeling that Claude is the best for programming, buts its pretty close.  I have been using Claude to help me to e.g. understand recent research in deep learning, so these models are definitely at the point where they can help you learn!  Note that:
* The university doesn't have a subscription to Claude.  So you can consider getting a personal subscription (I have one).  Other providers tend to have more/better free models available though.
* If you want to ask about something specific that turns up e.g. in the lecture notes, you can attach the lecture notes to your message to Claude!
* These models are pretty good in 99% of cases.  But like me/a TA, Claude can be wrong.  When these models are wrong, it is called a "hallucination" in deep learning research.  Some thoughts on that:
  - These models do not by default not have access to the internet (sometimes they do, but atm, you have to turn that on using a "search" or similar button).  So if you're asking about something super specific (e.g. something that only turns up in a few research papers), it may "misremember".  Try attaching some material (e.g. a paper on the topic) to your message to Claude!
  - These models can hallucinate if you ask leading questions.  For instance, if its impossible to do \<task\> in \<Python library\>, but you ask it  "How do I do \<task\> in \<Python library\>" anyway, it will often try anyway and give you a wrong solution.  Try to ask open-ended, non-leading questions.
* Be careful about which model you're asking.  Most of the providers have some good, expensive models and some less good, but cheaper models.  These platforms will often give free users some access to the good model, but quickly force you onto the less good model as you continue using it.

These models can supercharge your learning if you ask it about things you're confused about as you're learning.  As I am sure you are aware, they can also write code, solve exercises etc. for you.  I don't think we have any research on this, but that is likely to be detrimental to your learning.  And of course, in the exam, you won't have access to these models!  So be careful.  My advice is: use these models to help you learn more quicker, and think harder and deeper.  Definitely don't switch off brain and have them do stuff for you!

Finally, there's alot that these models can't do.  Despite the hype, it can't by itself build large programs/systems, nor can it write (interesting) research papers, and it definitely can't to any mechanical/civil engineering.  But they can dramtically accelerate experts as they do those things.  And they can definitely help you learn those things.  

Overall, these AI systems are some of the most powerful tools humanity has developed, and so learning to use them effectively is a critical skill!

## Other resources:

* [The little book of deep learning](https://fleuret.org/francois/lbdl.html)
* [3Blue1Brown (YouTube Channel)](https://www.youtube.com/c/3blue1brown)
* [Deep learning book](https://www.deeplearningbook.org)
* [Andrej Karpathy's course on building neural networks, from scratch, in code.](https://karpathy.ai/zero-to-hero.html)
* [Harvard Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)
* Usually searching Google for a given topic will give a bunch of blog posts on the subject (often in places like [Towards Data Science](https://towardsdatascience.com))

## Extra exercises

The exercises in the pdf notes and Colab notebooks are supposed to be complete.  But I have had a query about extra exercises.

If you find yourself in this position, the best exercise is to go through my Colab notebooks, looking mainly at my text (i.e. not the code).  Then close my notebook, and reproduce the code yourself.  If you can do that, you'll understand everything in the course really deeply.  And if you can reproduce the code in the non-examinable backprop notebook, let me know and I can chat to you about PhDs :-).

## Downloading the notes

To download the notes, use the download button highlighted with the red circle:

![button to download the notes](screenshot.png)

## Weekly material

#### Week 1: Prereqs and intro to PyTorch

We have students from quite a few different cohorts on this course.  So I'm going to try to go over at least some of the prerequistes here.  Even if the notes look easy, please do skim through to the end, and check out the exercises.  

In any case, there will definitely be material you haven't seen in notebook 1.2 (Introduction to PyTorch) and notebook 1.3 (GPUs with PyTorch).

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/1_prereqs/prereqs.pdf) | [notes video 1 (28:22)](https://uob.sharepoint.com/:v:/t/grp-LA/EcJ4IReynmZPpNCG2_kUMnIBguvkENLttVZaime8khzJKg) |
| | [notes video 2 (11:01)](https://uob.sharepoint.com/:v:/t/grp-LA/ESKjudaYaNlDulbC6qj6Ta8BWvM2NOWyxYcWVcE49eB0qQ) |
| | [notes video 3 (39:18)](https://uob.sharepoint.com/:v:/t/grp-LA/EWRUqCzSRNpAt-i2HtF-ArIBkkeeCretxXofdvK4WtWmOg) |
| | [notes video 4 (09:39)](https://uob.sharepoint.com/:v:/t/grp-LA/EfPjwXBcVi9MkbaicNi4qE8Bn7tgxawpb6aZ1pug9kETXA) |
| [Notebook 1.1: Introduction to Python](https://colab.research.google.com/drive/18jGWurFiWTrvcz_OLiWF46xuaTVvYDww?usp=sharing) | N/A |
| [Notebook 1.2: Introduction to PyTorch](https://colab.research.google.com/drive/1AV5pzM-9AIIDWldQZ6Id7XH8_yRGztGP?usp=sharing) | [notebook video (39:45)](https://uob.sharepoint.com/:v:/t/grp-LA/ESaKTjytko5Hjk4yMg-s1m8BNPJql5GrAGNf0foBA0i3FA) | 
| [Notebook 1.3: GPUs with PyTorch](https://colab.research.google.com/drive/1EjqE4eDioEdWJwWm_KnO0CPTds3LHKyC?usp=sharing) | N/A | 
| N/A | [Week 1 QA (23/24) (34:10)](https://uob.sharepoint.com/:v:/t/UnitTeams-EMAT31530-2023-24-TB-4-A/EXezUO44d2dBrZ2vyfWoyKIB4Cdcnj-MzMttYVCp3vGl_A) |


#### Week 2: Linear Regression

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/2_regression/regression.pdf) | [notes video 1 (24:57)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/ER4Iry8y6ndItNCFzORtK6YBOzMyo96zjKgcPogap8L0uA) |
| | [notes video 2 (13:30)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EaVCMXsQp_lHjfygzWUdCREBOzaCsmyDvj4z17sasdK85g) |
| | [notes video 3 (23:43)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EZbSaoApXjVOvEKCf1f-A7kBOHhWlk-Bs4o4KP_9RonDxw) |
| | [notes video 4 (27:27)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/Ee3CZ5XfG_NPsh_fCN4U-P0Bnfg0RPd63sa-N5tfzYSQsg) |
| [Notebook 2: Linear Regression](https://colab.research.google.com/drive/1wrgZfRJaWC-Hh_zgrDd-ubgdIAq0Qd_q?usp=sharing) | N/A |
| N/A | [Week 2 QA (19:40)](https://uob.sharepoint.com/:v:/t/UnitTeams-EMAT31530-2023-24-TB-4-A/EUD1dJvk0hZGhF1Ect2x9TYBd3ELuLXQLCgW1l0paMmZ5g) |

#### Week 3: Linear Classification

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/3_classification/classification.pdf) | [notes video 1 (21:56)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EdYiRNRTlEpDlyQwvCi7YzYBpESvfvI6xU-B9J5tS7-sDQ) |
| | [notes video 2 (24:31)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/Ebnm32pzEaJOrBq743-UxOsByQpQ8SqRjJVPg23m_mztQA) |
| | [notes video 3 (22:41)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EaFZZAf4Bg5FofmwNDjWRUoBhpMXIBYRuthKn_EsU99FpA) |
| [Notebook 3: Linear Classification](https://colab.research.google.com/drive/1XuazbDaJA88AJbdsm9mcw_foBfyQR2bH?usp=sharing) | N/A |
| N/A | [Week 3 QA (10:51)](https://uob.sharepoint.com/:v:/t/UnitTeams-EMAT31530-2023-24-TB-4-A/EWRi1FtGS2xOsO13s_aeY4sB_LjNVc8jvvW-OuOaObElUw) |

#### Week 4: NNs

This week, we introduce NNs!
This week is a bit unusual, as the notes are very short, with no exercises, but I expect the Python notebooks to be more challenging.
That's because mathematically defining NNs is somewhat straightforward.
However, understanding how PyTorch implements NNs requires a bit more thought, especially if you're going to understand things well enough to do modifications/tweaks for research/real-world problems!

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/4_nn/nn.pdf) | [notes video 1 (19:32)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EQgb2YmkGuxLvrFdM20sjV4BWlh8SBXTqW3O4m5pFiucZQ) |
| [Notebook 4.1: Python classes](https://colab.research.google.com/drive/1aERh1n1RdUVZJR_9VwPdEtNzdjqYB21c?usp=sharing) | N/A |
| [Notebook 4.2: NNs in PyTorch](https://colab.research.google.com/drive/1UyJM01YKfxszLffd-F2EU2yTFxmKb7e9?usp=sharing) | N/A |
| [Notebook 4.3: NNs with torch.nn](https://colab.research.google.com/drive/1dXEYDmW7Bu31rC2ejkNXfdTHfwVO_vrC?usp=sharing) | N/A |
| [Notebook 4.4: NN exercises](https://colab.research.google.com/drive/1zjH9hiu7Q85fWRuL5vfvMpfsOTv4q0tn?usp=sharing) | N/A |

#### Week 5: Backprop

The key bit of magic in PyTorch is the ability to compute gradients of the loss through arbitrary compute graphs.
PyTorch does this using the backprop algoritm, and the backprop algorithm to compute gradients is at the heart of all modern AI.
This might be a bit tougher than other weeks, as it involves going back-and-forth between the math and the code.
But once you really understand backprop, you'll really know (and be able to reason about) what goes on in modern AI.

Note that Notebook 5.2 is "formally" non-examinable, but should be super-useful in reinforcing the examinable material in the notes!

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/5_backprop/backprop.pdf) | [notes video 1 (16:55)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EU6TPdQ0WoBEqn3TeUAn-e0B0xPLT5Ypz-XHSTAA2A2Jlw?e=ahw3VY) |
| | [notes video 2 (23:40)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EaSlQHNHczhGs5JRfnAHxq4BWaM7OkuqXu5RTM8_tCtLzQ?e=fcNBJO) |
| | [notes video 3 (9:39)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/ERn7EiVTzMlLtDkf0YT5jB0BNd4fIOg-40RWu_VfOtJtSA?e=xWuOpq) |
| | [notes video 4 (7:00)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EdFpkDWzP5FBhQCbdWHIw0oBTp2W9CC24M-zS9rP3egnug?e=eBQbtQ) |
| | [notes video 5 (13:36)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EY6fxAUMxn9AjzGggKxO62QBqSBDqdjshA_Q28Zk-hEb9Q?e=FgVThQ) |
| [Notebook 5.1: Compute Graph](https://colab.research.google.com/drive/17aja1jqP-nrCZcQSTvMUVm1FkYrf_7ZM?usp=sharing) | N/A |
| [Notebook 5.2: Backprop](https://colab.research.google.com/drive/1A4Ne83U5Yp45Yivjo9baDC3LO7XyIhEs?usp=sharing) | N/A |

#### Week 6: Reading week!

#### Week 7: Optimization

Computing the gradients using backprop was the hard part.
But there still are a few tricks to using these gradients to quickly train NNs.
That's what this week is all about.


| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/7_optim/optim.pdf) | [notes video 1 (21:17)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EYMScaA6QF1NjGhnKxUmGWgBG-Ralhi-0hw-j1-IQ0hguw) |
| | [notes video 2 (7:13)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EVZfCjSaIBRPvcVmGFB69QkB9j14ZtIq4zyeEB8mDaFOmQ) |
| | [notes video 3 (23:16)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EVUUejzjQvhLr7cTbPe30RsBb1uex86gLs3grQF1v48neg) |
| | [notes video 4 (24:00)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/ERisNZHAOTpPtvwVGOjeBtYBJugU7BMwmf-Hn4aK7ez67w) |
| [Notebook 7.1 torch.optim](https://colab.research.google.com/drive/1S3bcYEUpeaXEMae0gRILxhIYN7EQcMHN?usp=sharing) | N/A |
| [Notebook 7.2 NNs for MNIST](https://colab.research.google.com/drive/1UA9-DSlbjoLp_vTYAi_bR7-6X6uvKMgi?usp=sharing) | N/A |


#### Week 8: Overfitting

This week is a bit unusual, because I'd advise looking at the CoLab notebook first.  That notebook introduces overfitting and cross-validation in linear models.
The pdf notes then go on to talk about overfitting in neural networks.

**Note that there are no exercises this week.**

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [Notebook 8 Overfitting](https://colab.research.google.com/drive/1_adhLa3YMOnnmIS0sKkYvjToisFuWr3Z?usp=sharing) | [notebook video (16:47)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/Eehq1IzytbFDpyT7l0N4z1kBzMOn7iQ3xCTPmzMI1JY6mw?e=IV8Op9) |
| [notes](notes/8_overfitting/overfitting.pdf) | [notes video 1 (17:01)](https://uob.sharepoint.com/:v:/t/grp-LA/Ee4MriT4lbtHs9c_x3bhaBwBGO2FLz-_Q5Xz85MDSwsSUw) |
|  | [notes video 2 (21:59)](https://uob.sharepoint.com/:v:/t/grp-LA/EQI-cw16ysBCovXNC0f2-IoBiMKDwYoXTdVWql4NkhJKqA) |

#### Week 9: CNNs

This week we'll look at architectures for neural networks for images.

**There are no exercises in the pdf notes this week, but there are exercises in the CoLab notebooks.**

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/9_cnn/cnn.pdf) | [notebook video 1 (28:33)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EVoYdfR1gdhIgJgyEPyUfDABpCfhDDkkshDNg8gj8CeVpg) |
| | [notebook video 2 (11:27)](https://uob-my.sharepoint.com/:v:/g/personal/ei19760_bristol_ac_uk/ERgnidh9URtDlUN0cHrthrgB6w_otIfknTJQsNyzAMi8YA) |
| | [notebook video 3 (18:24)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EQ1Kg8lHCqNFg055rGfnCCABQORuJkKhxcTchU31H9k5mA?e=uRUsme) |
| [Notebook 9.1 Convolutions](https://colab.research.google.com/drive/1A7nPFBzJLneS7e1FAMPbi8s2aCQ_SfG_?usp=sharing) | N/A |
| [Notebook 9.2 CNNs](https://colab.research.google.com/drive/1Myg8Ge9ubyRariUV1G0CGGbgiAheftuw?usp=sharing) | N/A |

#### Week 10: Large language models (LLMs)

This week we'll take a very high-level look at modern large language models.

**There are no exercises in the pdf notes this week, but there are exercises in the CoLab notebooks.**

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/10_llms/llm.pdf) | [notebook video 1 (8:30)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EUpV3cefSAFHmt72QTKa8VgBa4tmOA06c5goOgR5EOgRZA?e=gmusoy) |
| | [notebook video 2 (12:04)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EVfJV1I7gMhMkiwhiId0rcQBHDuOZCH6buF1XKQID3d0lA?e=lQMfup) |
| | [notebook video 3 (23:17)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EYk_H6-j8Q5DkTWFb2LOi3kBzw5bkt_14ViZVaUscrndVg?e=uENEu8) |
| | [notebook video 4 (21:02)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/ERqEcCBXSvRAt_U33IfMvaQBcxaoeg1NakEq8M3AjQ4ewQ?e=DjeTvM) |
| [Notebook 10.1 Strings](https://colab.research.google.com/drive/11fXTOUD_XJw3aRFQd2SQHxMFsLAqfuoq?usp=sharing) | N/A |
| [Notebook 10.2 Tokenization](https://colab.research.google.com/drive/1y-9Ezr6Kfn74QDtD-rqyF_JRH3zAEZNW?usp=sharing) | N/A |
| [Notebook 10.3 Attention](https://colab.research.google.com/drive/1wLaBNwbHT10UkvSuHfO6wgtrAqmqVkpg?usp=sharing) | N/A |


#### Week 11/12: Revision

There will be 2 hour revision sessions on 11am-1pm on Thursdays in QUEENS BLDG F.101a/b/c as usual.

<!--     -->
