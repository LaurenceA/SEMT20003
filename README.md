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
* There are pdf notes for every week of taught material.
* The pdf notes will _usually, but not always_ include questions.
* All questions will have worked answers.
* There will _usually, but not always_ be iPython notebooks (which are examinable), discussing practical aspects of training neural networks.  _It is critical for your understanding that you play around with the material in the notebooks.  Open up your own Colab notebook and enter the commands yourself; play with the commands; try things that are a little bit different!
* These iPython notebooks _occasionally_ have exercises.
* The concepts in the iPython notebooks are examinable.
* There will be videos of me going through the material in the pdf notes.
* Where appropriate there _may_ also be videos of me going through the iPython notebooks.  These videos won't add anything to the underlying notes/notebooks.  So if you read + understand the notes / notebooks, the videos are optional.  If you are going to look at the videos, then open up your own Colab notebook alongside and follow along.  Try the things that I'm doing.  Try something a bit different!  (Feel free to pause the video to do this!).
* The videos are not intended to add anything to the underlying material.  The exam is based on the notes/notebooks, _not_ the videos.  So if you're happy with the material in the notes/notebooks, you do not necessarily need to go through all the videos.
 
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
* These exams are in Christmas, and examine the taught material from TB1.
* I don't yet have confirmation on the exam format, but it will be 2 hours long.
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

#### Week 1

| Notes/Notebook | Video (if available) |
| ---- | ---- |
| [notes](notes/1_prereqs/prereqs.pdf) | [notes video 1 (28:22)](https://uob.sharepoint.com/:v:/t/grp-LA/EcJ4IReynmZPpNCG2_kUMnIBguvkENLttVZaime8khzJKg) |
| | [notes video 2 (11:01)](https://uob.sharepoint.com/:v:/t/grp-LA/ESKjudaYaNlDulbC6qj6Ta8BWvM2NOWyxYcWVcE49eB0qQ) |
| | [notes video 3 (39:18)](https://uob.sharepoint.com/:v:/t/grp-LA/EWRUqCzSRNpAt-i2HtF-ArIBkkeeCretxXofdvK4WtWmOg) |
| | [notes video 4 (09:39)](https://uob.sharepoint.com/:v:/t/grp-LA/EfPjwXBcVi9MkbaicNi4qE8Bn7tgxawpb6aZ1pug9kETXA) |
| [Notebook 1.1: Introduction to Python](https://colab.research.google.com/drive/18jGWurFiWTrvcz_OLiWF46xuaTVvYDww?usp=sharing) | N/A |
| [Notebook 1.2: Introduction to PyTorch](https://colab.research.google.com/drive/1AV5pzM-9AIIDWldQZ6Id7XH8_yRGztGP?usp=sharing) | [notebook video (39:45)](https://uob.sharepoint.com/:v:/t/grp-LA/ESaKTjytko5Hjk4yMg-s1m8BNPJql5GrAGNf0foBA0i3FA) | 
| [Notebook 1.3: GPUs with PyTorch](https://colab.research.google.com/drive/1EjqE4eDioEdWJwWm_KnO0CPTds3LHKyC?usp=sharing) | N/A | 
