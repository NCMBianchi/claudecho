# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-05-23

### Added
- Support for Claude 4 models (claude-opus-4-20250514, claude-sonnet-4-20250514)
- Web search capability via Anthropic's API
- Thinking mode parameter to see Claude's reasoning process

### Changed
- Updated default model to Claude Sonnet 4 (claude-sonnet-4-20250514)
- Improved error handling for web search responses
- Enhanced documentation for new features

## [1.0.0] - 2024-11-03

### Added
- Initial release as a fork from chatGPTclone repository
- Support for Anthropic's Claude API
- Interactive CLI functionality for Claude models
- Command line parameters for text input, temperature, max tokens, and model selection

### Changed
- Switched from OpenAI's API to Anthropic's API
- Modified CLI parameters to work with Claude's models
- Updated documentation for Claude API setup

### Fixed
- Added error handling for Anthropic's API responses, including credit balance checks
