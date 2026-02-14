# Agent Rules and Guidelines

## GitHub Workflow Rules

### Rule 1: Always Check GitHub Issues First

**CRITICAL REQUIREMENT:** Before starting any task that involves GitHub operations, you MUST:

1. **Check for related GitHub issues** using the GitHub MCP tools
2. **Review issue details** to understand:
   - The problem or feature request
   - Acceptance criteria
   - Any specific requirements or constraints
   - Related discussions or context
3. **Align your work** with the issue's requirements
4. **Reference the issue** in commits and pull requests

### How to Check GitHub Issues

Use the following GitHub MCP tools in this order:

```
1. fetch_github_issue - Fetch specific issue by number or URL
2. list_issues - List all open issues in the repository
3. search_issues - Search for issues with specific criteria
```

### Example Workflow

```
Step 1: User requests a task
Step 2: Check for related GitHub issues
Step 3: Review issue details and requirements
Step 4: Plan implementation based on issue
Step 5: Execute the task
Step 6: Reference issue in commits (e.g., "Fixes #123")
Step 7: Link issue in pull request description
```

### Commit Message Format

When working on GitHub issues, use these formats:

- `Fixes #123: Description of changes`
- `Closes #123: Description of changes`
- `Resolves #123: Description of changes`
- `Relates to #123: Description of changes`

### Pull Request Requirements

Every pull request MUST:

1. Reference the related issue number
2. Include issue context in the description
3. Address all acceptance criteria from the issue
4. Link to the issue using GitHub keywords (Fixes, Closes, Resolves)

## Benefits of This Approach

- ✅ Ensures work aligns with project requirements
- ✅ Maintains traceability between issues and code changes
- ✅ Prevents duplicate or unnecessary work
- ✅ Improves collaboration and communication
- ✅ Automatically closes issues when PRs are merged

## Exceptions

The only time you may skip checking GitHub issues:

- Emergency hotfixes (but create an issue immediately after)
- Documentation-only changes (though issues are still recommended)
- Initial repository setup

**Remember: When in doubt, check for an issue first!**