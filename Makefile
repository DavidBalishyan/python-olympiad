.PHONY: help 1 2 3 4

# Colors
RESET   = \033[0m
BOLD    = \033[1m
BLUE    = \033[1;34m
GREEN   = \033[1;32m
RED     = \033[1;31m
YELLOW  = \033[1;33m
CYAN    = \033[1;36m

help:
	@echo "$(BOLD)$(CYAN)Usage:$(RESET) make [target]"
	@echo ""
	@echo "  $(BOLD)$(BLUE)Targets:$(RESET)"
	@echo "  $(BOLD)$(YELLOW)help$(RESET) Show this help screen"
	@echo "  $(GREEN)1 to 4$(RESET)  run the corresponding files (./opt_*.py)"

1: 
	@python3 ./opt_1.py

2: 
	@python3 ./opt_2.py

3: 
	@python3 ./opt_3.py

4:
	@python3 ./opt_4.py

