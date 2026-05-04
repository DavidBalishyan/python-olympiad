##@ General
SHELL := /bin/bash
PYTHON := python3

.PHONY: help solve-1 solve-2 solve-3 solve-4 solve-mid-1 solve-mid-2 solve-mid-3 solve-mid-4 solve-senior-1 solve-senior-2 solve-senior-3 solve-senior-4 solve-junior-1 solve-junior-2 solve-junior-3 solve-junior-4 run-all clean


# Color output
RESET   := \033[0m
BOLD    := \033[1m
BLUE    := \033[1;34m
GREEN   := \033[1;32m
YELLOW  := \033[1;33m
CYAN    := \033[1;36m

help: ## Show this help message
	@printf "$(BOLD)$(CYAN)Python Olympiad Solutions$(RESET)\n"
	@printf "\n"
	@printf "$(BOLD)Usage:$(RESET)\n"
	@printf "  make [target]\n"
	@printf "\n"
	@printf "$(BOLD)$(CYAN)Available Targets:$(RESET)\n"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  $(BOLD)%-20s$(RESET) %s\n", $$1, $$2}'

##@ Solutions

solve-1: ## Run solution 1
	@$(PYTHON) opt_1.py

solve-2: ## Run solution 2
	@$(PYTHON) opt_2.py

solve-3: ## Run solution 3
	@$(PYTHON) opt_3.py

solve-4: ## Run solution 4
	@$(PYTHON) opt_4.py

solve-mid-1: ## Run mid solution 1
	@$(PYTHON) mid_opt_1.py

solve-mid-2: ## Run mid solution 2
	@$(PYTHON) mid_opt_2.py

solve-mid-3: ## Run mid solution 3
	@$(PYTHON) mid_opt_3.py

solve-mid-4: ## Run mid solution 4
	@$(PYTHON) mid_opt_4.py

solve-senior-1: ## Run senior solution 1
	@$(PYTHON) senior_opt_1.py

solve-senior-2: ## Run senior solution 2
	@$(PYTHON) senior_opt_2.py

solve-senior-3: ## Run senior solution 3
	@$(PYTHON) senior_opt_3.py

solve-senior-4: ## Run senior solution 4
	@$(PYTHON) senior_opt_4.py

solve-junior-1: ## Run junior solution 1
	@$(PYTHON) junior_opt_1.py

solve-junior-2: ## Run junior solution 2
	@$(PYTHON) junior_opt_2.py

solve-junior-3: ## Run junior solution 3
	@$(PYTHON) junior_opt_3.py

solve-junior-4: ## Run junior solution 4
	@$(PYTHON) junior_opt_4.py

run-all: solve-1 solve-2 solve-3 solve-4 solve-mid-1 solve-mid-2 solve-mid-3 solve-mid-4 solve-senior-1 solve-senior-2 solve-senior-3 solve-senior-4 solve-junior-1 solve-junior-2 solve-junior-3 solve-junior-4 ## Run all solutions

##@ Utilities

clean: ## Clean up Python cache and temporary files
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@printf "$(GREEN) Clean complete$(RESET)\n"

