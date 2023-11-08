from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup



class Questions(StatesGroup):
    name = State()
    age = State()
    gender = State()
    profession = State()
    hobby = State()


questions_router = Router()


@questions_router.message(Command('questions'))
async def start_questions(message: types.Message, state: FSMContext):
    await message.answer('Как вас завут?')
    await state.set_state(Questions.name)

@questions_router.message(F.text, Questions.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text.strip())

    await message.answer('Сколько вам лет?')
    await state.set_state(Questions.age)

@questions_router.message(F.text, Questions.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text.strip()
    if (not age.isdigit()):
        await message.answer('Введите только цифры')
    if (int(age) < 18 or int(age) > 40):
        await message.answer('Возраст от 18 до 40')
    else:
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Мужской"), types.KeyboardButton(text="Женский")],
            ]
        )

        await state.update_data(age=int(message.text))
        await message.answer("Какой у вас пол?", reply_markup=kb)
        await state.set_state(Questions.gender)

@questions_router.message(F.text, Questions.gender)
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text.strip()
    if (gender.lower() == "мужской" or gender.lower() == "женский"):
        kb = types.ReplyKeyboardRemove()
        await state.update_data(gender=gender)
        await state.set_state(Questions.profession)
        await message.answer('Какая у вас профессия?', reply_markup=kb)
    else:
        await message.answer('Введите "Мужской" или "Женский"')

@questions_router.message(F.text, Questions.profession)
async def process_profession(message: types.Message, state: FSMContext):
    await state.update_data(profession=message.text.strip())

    await message.answer('Чем вы увлекаетесь?')
    await state.set_state(Questions.hobby)

@questions_router.message(F.text, Questions.hobby)
async def process_hobby(message: types.Message, state: FSMContext):
    await state.update_data(hobby=message.text.strip())
    await message.answer('Спасибо за опрос!')

