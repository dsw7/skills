.PHONY = sync

sync:
	@rsync -av --delete skills/ ~/.claude/skills
