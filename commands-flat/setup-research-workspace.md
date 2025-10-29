Please assist the user by setting up a structured research workspace in this repository.

The user has started this repo to run some deep research into a specific topic.

Please:

- Create /prompts with subfolders /drafting /run /queue
- Create CLAUDE.md instructing yourself of its purpose and referencing the files created 
- Create /analysis for saving your analyses as markdown documents 
- Create /context for the user to supply additional context. At the base of this subfolder, create index.md 
- Create scratchpad for the user to jot down notes 

For CLAUDE.md, instruct this workflow:

- User will create prompts in the prompt folder 
- Claude will research referencing the context as well as the prompt on each turn
- Claude will write out analyses files in analysis with descriptive names 
- When Claude has finished analysis, Claude will move the prompt into the run subfolder
- If Claude finds a number of prompts in queue it should run them sequentially 