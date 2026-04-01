##@ General
SHELL := /bin/bash
PYTHON := python3

.PHONY: help solve-1 solve-2 solve-3 solve-4 run-all clean


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

run-all: solve-1 solve-2 solve-3 solve-4 ## Run all solutions

##@ Utilities

clean: ## Clean up Python cache and temporary files
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@echo "$(GREEN) Clean complete$(RESET)"

