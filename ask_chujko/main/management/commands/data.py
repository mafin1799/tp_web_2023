from django.core.management.base import BaseCommand
from faker import Faker
import random

from django_bulk_update.manager import BulkUpdateManager

from ask_chujko.main.models import *

USERS_COUNT = 10500
QUESTIONS_COUNT = 100500
ANSWERS_COUNT = 1050000
TAGS_COUNT = 10000
VOTES_COUNT = 2000500


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_profiles()
        self.create_questions()
        self.create_answers()
        self.create_tags()
        self.create_tags_questions_link()
        self.create_votes()

    def create_profiles(self):
        profiles = []
        faker = Faker()
        for i in range(USERS_COUNT):
            profiles.append(Profile(nickname=faker.word()))
        Profile.objects.bulk_create(profiles, USERS_COUNT)

    def create_questions(self):
        questions = []
        faker = Faker()
        users = Profile.objects.all()
        for i in range(QUESTIONS_COUNT):
            questions.append(
                Question(title=faker.sentence(), text=faker.text(), date_published=faker.date_time_this_year(),
                         is_published=True, author=random.choice(users)))
        Question.objects.bulk_create(questions, QUESTIONS_COUNT)

    def create_answers(self):
        answers = []
        faker = Faker()
        questions = Question.objects.all()
        users = Profile.objects.all()
        for i in range(ANSWERS_COUNT):
            answers.append(Answer(text=faker.text(), correct=False, question=random.choice(questions),
                                  date_published=faker.date_time_this_year(), author=random.choice(users)))
        Answer.objects.bulk_create(answers, ANSWERS_COUNT)

    def create_tags(self):
        tags = []
        faker = Faker()
        for i in range(TAGS_COUNT):
            tags.append(Tag(tag=faker.word() + str(i)))
        Tag.objects.bulk_create(tags, TAGS_COUNT)

    def create_tags_questions_link(self):
        questions = Question.objects.all()
        tags = Tag.objects.all()
        for tag in tags:
            tag_questions = []
            for _ in range(random.randint(10, 50)):
                question = random.choice(questions)
                if question not in tag_questions:
                    tag_questions.append(question)
            tag.question.add(*tag_questions)
        Tag.objects.bulk_update(tags, update_fields=['question'])

    def create_votes(self):
        questions = Question.objects.filter(pk__lte=10500)
        users = Profile.objects.all()
        answers = Answer.objects.filter(pk__lte=10500)
        i = 0
        votesCount = 0
        while (votesCount < 1000000):
            user = users[i]
            votes = []
            for question in questions:
                like = random.choice([-1, 1])
                votes.append(Like(author=user, votes=like, content_object=question))
                votesCount += 1
                question.rating += like
            for answer in answers:
                like = random.choice([-1, 1])
                votes.append(Like(author=user, votes=like, content_object=answer))
                votesCount += 1
                answer.rating += like

            Like.objects.bulk_create(votes)
            i += 1
        for question in questions:
            question.save(update_fields=['rating'])
        for answer in answers:
            answer.save(update_fields=['rating'])
