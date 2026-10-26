from aiogram import Router, types, F
rt = Router()
@rt.message(F.photo)
async def test(msg: types.Message):
   await msg.answer("siz rasm yubordingiz")

@rt.message(F.animation)
async def test(msg: types.Message):
   await msg.answer("siz gif yubordingiz")

