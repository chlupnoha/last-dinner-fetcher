# CLAUDE.md - AI Assistant Guide for last-dinner-fetcher

## Project Overview

**Project Name:** last-dinner-fetcher
**Repository:** chlupnoha/last-dinner-fetcher
**Current Status:** Initial setup phase
**Last Updated:** 2025-11-17

### Purpose
This project appears to be a service/tool for fetching and managing dinner-related information. The exact scope is being defined, but based on the name, it likely involves:
- Fetching dinner suggestions or menus
- Tracking meal history
- Integrating with food/restaurant APIs
- Potentially providing recommendations

## Repository Structure

```
last-dinner-fetcher/
├── README.md           # Basic project documentation
├── CLAUDE.md          # This file - AI assistant guide
└── .git/              # Git version control
```

### Expected Future Structure

As the project develops, anticipate this structure:

```
last-dinner-fetcher/
├── src/               # Source code
│   ├── index.js/ts    # Entry point
│   ├── api/           # API integration modules
│   ├── services/      # Business logic
│   ├── models/        # Data models
│   └── utils/         # Utility functions
├── tests/             # Test files
│   ├── unit/          # Unit tests
│   └── integration/   # Integration tests
├── config/            # Configuration files
├── docs/              # Additional documentation
├── .github/           # GitHub workflows and templates
├── package.json       # Node.js dependencies (if Node.js)
├── .gitignore         # Git ignore rules
├── .env.example       # Environment variable template
└── README.md          # Project documentation
```

## Development Workflow

### Git Branching Strategy

**Current Branch:** `claude/claude-md-mi3fkept0bweg91n-01FmKYAWRZ8QzHS1aq52dG4v`

**Branch Naming Convention:**
- Feature branches: `feature/<feature-name>`
- Bug fixes: `fix/<bug-description>`
- Claude AI branches: `claude/claude-md-<session-id>`

### Commit Guidelines

1. **Commit Message Format:**
   ```
   <type>: <subject>

   <body (optional)>
   ```

2. **Types:**
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `refactor`: Code refactoring
   - `test`: Adding or updating tests
   - `chore`: Maintenance tasks
   - `style`: Code style changes (formatting, etc.)

3. **Examples:**
   ```
   feat: add API client for restaurant data
   fix: handle null values in dinner response
   docs: update README with setup instructions
   ```

### Git Operations Best Practices

**Pushing Changes:**
```bash
git push -u origin <branch-name>
```
- Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s) on network errors
- Branch names must start with 'claude/' and match session ID for AI assistant work

**Fetching/Pulling:**
```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```
- Use same retry logic for network failures

## Coding Conventions

### General Principles

1. **Code Quality:**
   - Write clean, readable, and maintainable code
   - Follow DRY (Don't Repeat Yourself) principle
   - Use meaningful variable and function names
   - Keep functions small and focused (single responsibility)

2. **Error Handling:**
   - Always handle errors gracefully
   - Provide informative error messages
   - Log errors appropriately
   - Don't expose sensitive information in errors

3. **Security:**
   - Never commit secrets, API keys, or credentials
   - Use environment variables for configuration
   - Validate all user inputs
   - Be aware of common vulnerabilities (OWASP Top 10):
     - SQL Injection
     - XSS (Cross-Site Scripting)
     - Command Injection
     - Insecure Deserialization
     - Authentication/Authorization issues

4. **Testing:**
   - Write tests for new features
   - Maintain test coverage above 80%
   - Test edge cases and error conditions
   - Use descriptive test names

### Language-Specific Conventions

**If JavaScript/Node.js:**
- Use ES6+ features (const/let, arrow functions, async/await)
- Follow Airbnb or Standard style guide
- Use meaningful destructuring
- Prefer async/await over callbacks

**If TypeScript:**
- Enable strict mode
- Define interfaces for data structures
- Avoid using `any` type
- Use type inference where appropriate

**If Python:**
- Follow PEP 8 style guide
- Use type hints (Python 3.6+)
- Write docstrings for functions/classes
- Use virtual environments

### File Organization

1. **Imports:**
   - Group imports: standard library, third-party, local
   - Sort alphabetically within groups
   - Remove unused imports

2. **Functions/Classes:**
   - Public functions/methods first
   - Private/helper functions last
   - Document complex logic

3. **Constants:**
   - Use UPPER_CASE for constants
   - Group related constants together
   - Consider separate config file for many constants

## AI Assistant Guidelines

### Before Making Changes

1. **Understand Context:**
   - Read relevant files completely
   - Check existing patterns and conventions
   - Review recent commits for context

2. **Plan Your Work:**
   - Use TodoWrite tool for multi-step tasks
   - Break complex tasks into smaller steps
   - Communicate your plan before executing

3. **Check Dependencies:**
   - Verify all required files exist
   - Check for related code that might be affected
   - Consider backward compatibility

### During Development

1. **Tool Usage:**
   - Use Read before Edit or Write
   - Use specialized tools (Read/Edit/Write) instead of bash for file operations
   - Run multiple independent operations in parallel
   - Use Task tool for complex searches or exploration

2. **Code Changes:**
   - Make minimal, focused changes
   - Preserve existing code style
   - Update tests when changing functionality
   - Add comments for complex logic

3. **Testing:**
   - Run existing tests before and after changes
   - Add new tests for new functionality
   - Fix any failing tests before committing

### After Development

1. **Verification:**
   - Review all changes
   - Ensure tests pass
   - Check for unintended side effects
   - Verify no sensitive data is included

2. **Documentation:**
   - Update relevant documentation
   - Add/update code comments
   - Update CLAUDE.md if workflow changes

3. **Committing:**
   - Write clear commit messages
   - Stage related changes together
   - Follow commit message format
   - Push to correct branch

## Common Tasks

### Setting Up the Project

```bash
# Clone repository
git clone <repository-url>
cd last-dinner-fetcher

# Install dependencies (when package.json exists)
npm install
# or
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with appropriate values

# Run tests
npm test
# or
pytest
```

### Adding a New Feature

1. Understand the requirement
2. Create TodoWrite task list
3. Explore relevant existing code
4. Implement the feature
5. Add/update tests
6. Update documentation
7. Commit and push

### Fixing a Bug

1. Reproduce the bug
2. Locate the problematic code
3. Write a test that exposes the bug
4. Fix the issue
5. Verify test passes
6. Check for similar issues elsewhere
7. Commit with descriptive message

### Refactoring Code

1. Ensure tests exist and pass
2. Make incremental changes
3. Run tests after each change
4. Maintain backward compatibility
5. Update documentation if needed
6. Commit with clear refactoring description

## Project-Specific Notes

### Current State
- ✅ Repository initialized
- ✅ Basic README created
- ✅ CLAUDE.md created
- ⏳ Project structure to be defined
- ⏳ Core functionality to be implemented
- ⏳ Dependencies to be added
- ⏳ Tests to be set up

### Next Steps
1. Define project requirements and scope
2. Choose technology stack (Node.js, Python, etc.)
3. Set up project structure
4. Add dependencies and configuration
5. Implement core functionality
6. Add tests
7. Set up CI/CD pipeline

### Questions to Answer
- What is the primary data source for dinner information?
- Is this a CLI tool, web service, or library?
- What APIs or services will be integrated?
- What is the expected output format?
- Who is the target audience?

## Resources

### Documentation Standards
- Use Markdown for documentation
- Include code examples
- Keep documentation up-to-date
- Document public APIs thoroughly

### Useful Commands

```bash
# View git status
git status

# View recent commits
git log --oneline -10

# View differences
git diff

# Create new branch
git checkout -b feature/new-feature

# Amend last commit (only if not pushed)
git commit --amend

# View remote info
git remote -v
```

## Troubleshooting

### Common Issues

**Git Push Fails with 403:**
- Verify branch name starts with 'claude/' for AI assistant work
- Check network connectivity
- Retry with exponential backoff

**Merge Conflicts:**
- Fetch latest changes from origin
- Resolve conflicts manually
- Test after resolving
- Commit resolution

**Tests Failing:**
- Run tests individually to isolate issue
- Check for environment differences
- Verify dependencies are installed
- Review recent changes

## Contact & Support

- Repository Owner: chlupnoha
- For issues: Create GitHub issue
- For questions: Check documentation first, then ask repository owner

---

**Note for AI Assistants:** This document should be updated as the project evolves. When significant changes occur to the project structure, workflow, or conventions, update this file accordingly and include the update in your commit.
