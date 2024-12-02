from .context import context

MOD_NAME = 'ReallyShadowheart'
MOD_UUID = 'e49a2415-9dda-48ad-84c9-0abd35686529'

ctx = context(MOD_NAME, MOD_UUID)
env = ctx.env
tool = ctx.tool
files = ctx.files
root_path = ctx.root_path
