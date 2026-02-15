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
Step 3: Confirm issue details and requirements with users
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
## Managing GitHub Issue Status with MCP

### Issue Status Labels

GitHub issues should be tracked using status labels throughout their lifecycle:

- **backlog** - Issue identified but not yet prioritized
- **ready** - Issue is ready to be worked on
- **in-progress** - Work is actively being done
- **in-review** - Work is complete and under review (PR created)
- **done** - Work is completed and merged

### How to Update Issue Status Using MCP Tools

Use the GitHub MCP `issue_write` tool to update issue labels and status:

#### Update Issue Labels (Change Status)

```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "repository-owner",
  "repo": "repository-name",
  "issue_number": 123,
  "labels": ["in-review"]
}
</arguments>
</use_mcp_tool>
```

#### Add Status Comment

Always add a comment when changing status to provide context:

```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>add_issue_comment</tool_name>
<arguments>
{
  "owner": "repository-owner",
  "repo": "repository-name",
  "issue_number": 123,
  "body": "## Status Update\n\nMoving to **in-review** status.\n\n**PR:** #456\n**Changes:** Brief description of what was done"
}
</arguments>
</use_mcp_tool>
```

### Issue Status Workflow

**Complete workflow for managing issue status:**

#### 1. Backlog → Ready
When issue is prioritized and ready to work:
```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "owner",
  "repo": "repo",
  "issue_number": 123,
  "labels": ["ready"]
}
</arguments>
</use_mcp_tool>
```

#### 2. Ready → In-Progress
When starting work on the issue:
```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "owner",
  "repo": "repo",
  "issue_number": 123,
  "labels": ["in-progress"]
}
</arguments>
</use_mcp_tool>
```

Add comment:
```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>add_issue_comment</tool_name>
<arguments>
{
  "owner": "owner",
  "repo": "repo",
  "issue_number": 123,
  "body": "Starting work on this issue."
}
</arguments>
</use_mcp_tool>
```

#### 3. In-Progress → In-Review
When work is complete and PR is created:
```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "owner",
  "repo": "repo",
  "issue_number": 123,
  "labels": ["in-review"]
}
</arguments>
</use_mcp_tool>
```

Add comment with PR details:
```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>add_issue_comment</tool_name>
<arguments>
{
  "owner": "owner",
  "repo": "repo",
  "issue_number": 123,
  "body": "## Work Complete ✅\n\n**Status:** In Review\n**PR:** #456\n\nAll requirements implemented and ready for review."
}
</arguments>
</use_mcp_tool>
```

#### 4. In-Review → Done
When PR is merged and work is complete:
```xml
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "owner",
  "repo": "repo",
  "issue_number": 123,
  "state": "closed",
  "state_reason": "completed",
  "labels": ["done"]
}
</arguments>
</use_mcp_tool>
```

### Best Practices for Status Management

1. **Always update status** when transitioning between workflow stages
2. **Add comments** explaining the status change and providing context
3. **Link PRs** when moving to in-review status
4. **Keep labels consistent** - use only one status label at a time
5. **Close issues** only when work is fully merged and verified (done status)

### Example: Complete Status Workflow

```xml
<!-- Step 1: Move to in-progress when starting work -->
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "hagsmand",
  "repo": "bob-demo-project",
  "issue_number": 2,
  "labels": ["in-progress"]
}
</arguments>
</use_mcp_tool>

<!-- Step 2: Move to in-review when PR is created -->
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "hagsmand",
  "repo": "bob-demo-project",
  "issue_number": 2,
  "labels": ["in-review"]
}
</arguments>
</use_mcp_tool>

<!-- Step 3: Add comment with PR link -->
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>add_issue_comment</tool_name>
<arguments>
{
  "owner": "hagsmand",
  "repo": "bob-demo-project",
  "issue_number": 2,
  "body": "## Status: In Review\n\n**PR:** #3\n**Branch:** feature/flask-migration\n\nWork completed and ready for review."
}
</arguments>
</use_mcp_tool>

<!-- Step 4: Close and mark as done after PR merge -->
<use_mcp_tool>
<server_name>github</server_name>
<tool_name>issue_write</tool_name>
<arguments>
{
  "method": "update",
  "owner": "hagsmand",
  "repo": "bob-demo-project",
  "issue_number": 2,
  "state": "closed",
  "state_reason": "completed",
  "labels": ["done"]
}
</arguments>
</use_mcp_tool>
```

### Status Label Reference

| Status | Description | When to Use |
|--------|-------------|-------------|
| `backlog` | Issue identified, not prioritized | Initial issue creation |
| `ready` | Ready to be worked on | After prioritization |
| `in-progress` | Actively being worked on | When starting work |
| `in-review` | Under review (PR created) | When PR is created |
| `done` | Completed and merged | After PR merge |


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