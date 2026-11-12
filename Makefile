sync_dir := /Volumes/CIRCUITPY

.PHONY: sync
sync:
	./send_to.sh $(sync_dir)
