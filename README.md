# EMAT31530: Introduction to AI
The course will introduce AI, with a focus on neural networks in PyTorch.

## Staff
- [Laurence Aitchison](http://www.gatsby.ucl.ac.uk/~laurence/) [laurence.aitchison@bristol.ac.uk] (unit director)

## Teaching Block Structure
* This course runs across TB1 + TB2.
* TB1: all the teaching happens in TB1.
* TB2: there is a group project in the first half of TB2.

## Prerequisites
EMAT20011, EMAT10006 (or equivalent units, i.e good knowledge and experience with Python and basic statistics)

## Course Structure

The course is taught in a "flipped classroom model".  So there are no in-person lectures (we wouldn't be able to schedule them anyway given the wide range of cohorts on the course).  Instead, there are extensive pdf notes, iPython notebooks and videos.  Then, you can ask questions through the 2-hour weekly TA-led problem classes, and the 1-hour weekly lecturer-led QA session (see Feedback below).

## Course Materials for TB1:
Course materials for each week will be posted here on Monday.  Course materials each week will include some combination of:
* Notes
  - There are pdf notes for every week of taught material.
  - The notes are often long-ish, but that's only because I'm trying to be _thorough_ (e.g. I'm trying to include all the steps in derivations).  So the notes shouldn't in general be very dense.
  - The pdf notes will _usually, but not always_ include questions.
  - All questions will have worked answers.
* Notebooks
  - Each week, there will _usually, but not always_ be iPython notebooks, discussing practical aspects of training neural networks.
  - These iPython notebooks _occasionally_ have exercises.
  - The concepts in the iPython notebooks are examinable.
  - You don't learn code (well) by just reading.  Even if I haven't done exercises, open up your own Colab notebook alongside and type the code in to follow along.  Try the things that I'm doing.  Try something a bit different!
* Videos
  - There are always videos of me going through the pdf notes, and may sometimes be videos of me going through the iPython notebooks.
  - _Watching the videos isn't necessary!!!_  The videos just go through (slowly and thoroughly) the material in the underlying pdf notes / iPython notebook.  So if you read + understand the underlying notes / notebooks, the videos are not necessary.
  - To reiterate, the exam is based on the notes/notebooks, _not_ the videos.
 
## Feedback: 
* TA-led labs/problem classes on Fridays 11-1 in MVB 1.11.
  - *These labs/problem classes are the primary route for feedback on all aspects of the course, including lectures, notes, questions, iPython notebooks, past exams and the group coursework!!!!*
  - There is no extra content for these classes.  You're expected to bring questions from the material from that week, and ask the TAs.  The TAs will be wandering around the room.
* Online, lecturer-led QA sessions, Thursday 4-5pm in TB1.  Held as a Teams meeting from the course Team.
  - Again, this is for feedback on all parts of the course, including lectures, notes, questions, iPython notebooks, past exams and the group coursework.
  - A couple of you will have clashes.  Apologies.  Timetabling have worked hard to minimize clashes, but it isn't actually possible to eliminate clashes, given the wide range of cohorts on the course.  The sessions will be recorded, and you can e.g. ask some else to submit your question.
  - Please do remind me if I forget to record!

## Why PyTorch
All the notebooks are going to be in [PyTorch](https://pytorch.org).  These days, you _need_ to know PyTorch if you're doing AI:
* PyTorch is currently the leading AI library, both for academic research, and industry.
* Fantastic docs + tutorials + libraries than any other library
* Pythonic and hackable: you can look at + modify the source for just about anything
* PyTorch is great for learning AI, because it exposes alot of the underlying concepts, and doesn't hide them under abstractions.
* As we'll see, you can use PyTorch as GPU-enabled-numpy, so it is useful for many applications outside of traditional AI.

Other points:
* You're going to need PyTorch for the group project.
* You won't need to install PyTorch.  All the iPython notebooks in the taught material are presented using [Google Colab](https://colab.research.google.com).  And you can do your group project there too!

## Exam (50% of total mark):
* These exams are in the standard TB1 assessment period, and examine the taught material from TB1.
* The exam will be a 2 hour, 15 question, multiple choice, in-person exam.
* The exam is mainly based on theory/maths.  But material in the iPython notebooks will be examinable.  But the exam will be paper-based, so you won't actually need to do any coding.  For instance, the question might give a piece of code, and you have to work out the shape of a tensor in that code.
* Things have changed quite alot since last year, so previous EMAT31530 exams are no longer relevant.
* I will post a practice exam once details are available.
* The exam will focus on the _concepts_ rather than requiring you to learn specific math equations / PyTorch functions.  So focus on understanding the underlying concepts, and don't worry too much about very low-level details.  Exactly what I mean by that will be more obvious once the practice exam is available.

## Group coursework (50% of total mark):
There will be a group coursework in TB2, which will run roughly for the first half of the teaching block.  Details are again not yet nailed down, and I will announce as soon as information is available.

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
| N/A | [Week 1 QA (34:10)](https://uob.sharepoint.com/:v:/t/UnitTeams-EMAT31530-2023-24-TB-4-A/EXezUO44d2dBrZ2vyfWoyKIB4Cdcnj-MzMttYVCp3vGl_A) |

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


| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/5_backprop/backprop.pdf) | [notes video 1 (20:06)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EbbvdyCRZRJMoa9YBt0SLKYB7R5FSZqzQPk6dr9352uomw) |
| | [notes video 2 (15:48)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/ESL-W0p5tYJPriVWJrZdzzkBwHxvFDyGkiQKhHyPrAJIOQ) |
| | [notes video 3 (15:04)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EUow4gEqGHNNi7kRqL4oussB1Se_WQpl2qExDJx1F0Uv7w) |
| | [notes video 4 (20:59)](https://uob.sharepoint.com/:v:/t/grp-LAlectures/EZH1PMMjpXhKtu9rzWHtQSYBkQyrUV1qs_-48zrNNx7VBA) |
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

