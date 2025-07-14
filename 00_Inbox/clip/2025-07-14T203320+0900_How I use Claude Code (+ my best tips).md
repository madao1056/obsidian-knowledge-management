---
title: "How I use Claude Code (+ my best tips)"
source: "https://www.builder.io/blog/claude-code"
author:
  - "[[Steve Sewell]]"
published: 2025-07-11
created: 2025-07-14
description: "I switched from Cursor's agents to Claude Code weeks ago and I'm not going back. Here's how I use it and my best practical tips"
tags:
  - "Inbox_webcliper"
---
[‹ Back to blog](https://www.builder.io/blog)

#### ai

#### 2025年7月11日

#### Written By Steve Sewell

![](https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fd70b6e7b9e6a480e8ddaf1491742deb4?format=webp&width=100)

I've been a Cursor power user for over a year. I wrote [the guide to Cursor tips](https://www.builder.io/blog/cursor-tips) that thousands of developers reference every week. I've gone deep down the rabbit hole on every Cursor power feature and agent mode best practice.

And I've abandoned it all for Claude Code.

For weeks now, I've been living entirely in Claude Code instead of Cursor's agents. And honestly, there's no going back.

Here's how I use Claude Code and my best tips for getting the most out of it

## Use the VS Code extension

First things first: install the Claude Code extension. It works with VS Code, Cursor, and probably Windsurf too. Don't expect fireworks, it's basically just a launcher. But it makes opening Claude Code dead simple, and you can run multiple instances in parallel in different panes in your IDE as long as they're working on different parts of your codebase.

<video><source type="video/mp4" src="https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2F79e3ebc00fee48d6aa3cb003bfb689a2?alt=media&amp;token=69245f9d-23bc-4fb4-94a0-0ad509743e73&amp;apiKey=YJIGb4i01jvw0SRdL5Bt"></video>

I still use Cursor for quick Command+K completions and tab completions. But the agent sidebar? I only touch it when Claude is down.

The weird thing is how my workflow has evolved. I used to have Claude as a small sidebar while coding in the main editor. Now I default to Claude first and only peek at code when reviewing changes. It's become my primary interface, not my secondary one.

## The terminal UI is good

Yeah, I was skeptical too. A terminal interface for chat-based code editing? Sounds like a step backward. But Anthropic did a decent job with it.

You can @-tag files easily, use slash commands (which are helpful), and choose exactly what context to include. I mostly stick with Opus unless it's having one of its moments, then I switch to Sonnet. Most people should probably just use the defaults - it'll use Opus until you hit 50% usage, then switch to Sonnet for cost efficiency.

<video><source type="video/mp4" src="https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2F0628b2e3ebf84052813f69eb235377d6?alt=media&amp;token=d301f867-be8b-4dd5-8d23-71d7c15ea8f8&amp;apiKey=YJIGb4i01jvw0SRdL5Bt"></video>

Pro tip: use `/clear` often. Every time you start something new, clear the chat. You don't need all that history eating your tokens, and you definitely don't need Claude running compaction calls to summarize old conversations. Just clear it and move on.

The up arrow lets you navigate back through past chats, even from previous sessions. Handy when you need to reference something from yesterday.

Here's the most annoying thing about Claude Code: it asks permission for everything. You type a prompt, it starts working, you go check Slack, come back five minutes later, and it's just sitting there asking "Can I edit this file?"

Yes, you can edit files. That's literally the point.

Same with running basic commands. "Can I run lint?" YES. My god, just yes.

There's a solution though. Every time I open Claude Code, I hit Command+C and run `claude --dangerously-skip-permissions`. It's not as dangerous as it sounds — think of it as Cursor's old yolo mode. Could a rogue agent theoretically run a destructive command? Sure. Have I seen it happen in weeks of usage? Never.

Your call on the risk tolerance, but I sleep fine at night.

## The GitHub integration is actually useful

One of the cooler slash commands is `/install-github-app`. After you run it, Claude will automatically reviews your PRs.

This is actually useful because as you use more AI tools, your PR volume increases. And honestly? Claude often finds bugs that humans miss. Humans nitpick variable names. Claude finds actual logic errors and security issues.

<video><source type="video/mp4" src="https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2Feb25e8138776413181ca983d4e8b2808?alt=media&amp;token=496b0370-8d1c-4bbe-a2e6-4650b95076f3&amp;apiKey=YJIGb4i01jvw0SRdL5Bt"></video>

The key is customizing the review prompt. Out of the box, it's way too verbose and comments on every little thing. Claude will add a `claude-code-review.yml` file with a prompt already in it. Here's what I use instead:

The original issue we found with this tool is it was really verbose. It would comment on all kinds of nuanced, unimportant things and write a whole essay on every PR. What we really care about most is bugs and potential vulnerabilities. So we tell it exactly that, and to be concise.

There's other cool stuff it can do too, like pull comments from a GitHub pull request and address them, or review a pull request directly.

## The quirks you need to know

Since it's a terminal interface, there are some non-obvious behaviors:

- **Shift+Enter** doesn't work by default for new lines. Just tell Claude to set up your terminal with `/terminal-setup` and it'll fix it for you.
- **Dragging files in** normally opens them in a new tab like in Cursor or VS Code. Hold Shift while dragging to reference them properly in Claude.
- **Pasting images** from clipboard doesn't work with Command+V. Use Control+V instead. Took me forever to figure that out.
- **Stopping Claude** isn't Control+C (that just exits entirely). Use Escape to actually stop Claude.
- **Jumping to previous messages**: Escape twice shows a list of all previous messages you can jump back to.

There's also a Vim mode if you're into that. I'm not.

## Claude Code handles large codebases better

Here's the real difference: we have a React component at Builder that's 18,000 lines long. (Don't @ me about code organization, I know.) No AI agent has ever successfully updated this file except Claude Code.

When using Cursor, I still find a lot of little hiccups. It has trouble resolving patches, has to rewrite files often, and really struggles to update extremely large files.

This isn't just about file size, Claude Code works great with complex tasks. I find it gets stuck incredibly rarely (I'm not even sure if I've noticed it at all). With Cursor, I feel like I have to babysit it more, and when it gets stuck, I have to stop it and realize maybe this wasn't a good task to ask.

Claude is also exceptionally good at navigating large codebases, searching for patterns, understanding relationships between different parts of the code, components, shared state, stuff like that. It's honestly kind of incredible.

![](https://www.youtube.com/watch?v=n7iT5r0Sl_Y)

## The economics make sense

Think about it: Cursor built a general-purpose agent that supports multiple models. They need a whole team for that, plus they trained custom models, plus they need to make a profit on top of paying Anthropic for the underlying models.

Anthropic definitively makes the best coding models, and they make Claude Code the best at using those models. When they hit challenges with Claude Code, they go and make the model better.

![image.png](https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2Ff1d62f97d20e47d581d4a3b931ead978?format=webp&width=100)

They know everything about how the model works, how it's trained, and how to use it in depth. They continue to train the model to work well with what they need for Claude Code.

It also means Anthropic can give you the most possible value for the least possible price because you only have to worry about paying them.

They can compete on giving you maximum access to models like Opus without situations like Cursor has, where Cursor has to make money too.

![image.png](https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F593db63d4a154b53b9122412770e4e0c?format=webp&width=100)

It's like buying direct from the manufacturer instead of through a reseller. Of course it's better.

## The pricing is reasonable

I pay for the max plan at $100/month. If you think a shockingly intelligent coder working 24/7 isn't worth $100/month, you need to look at what you charge for your own time. Look at what a human costs per hour for engineering, regardless of where you look in the world, it's orders of magnitude more than that.

Any manager doing that math will see it's overwhelmingly worth it, even at the highest possible pricing tiers.

## The queuing system is handy dandy

One feature I can't live without: message queuing. You can type multiple prompts and Claude will work through them intelligently.

What I used to do is create a notepad and start drafting other prompts that I wanted to do. Then when I saw one was done, I'd go paste the next one and hit enter. That's what I did with Cursor, which is really annoying because I'll usually go about my day, answer Slack messages, answer email, do something else, and come back to see the agent's been idle for who knows how long.

<video></video>

Now I just queue everything up: "Add more comments," "Actually also …," "And … too." Claude is really smart about knowing when it should actually run those things. If it needs feedback from you, it's not going to automatically run the queued messages. It's a pretty smart system, but when it's wrapped up something, it'll start addressing them when it makes sense.

You can queue up a lot, go about your day, and in a lot of cases just come back to a ton of work done in a good and smart way. But check it from time to time because it might need your input.

## The customization goes pretty deep

Claude Code supports custom hooks, slash commands, and project-specific configuration. The cool part? You can have Claude build these for you.

I asked Claude to add a couple default hooks, commands, and settings. It looked at my project and created a settings file that I can easily edit, with a few notable highlights:

It added a `CLAUDE.md` file, which gives a bit of project overview and some key commands that it should know about. This prevents it from having to figure that out each time and scan the codebase for "is there a build command or a lint command?" It always has awareness of that.

It adds some hooks for what code should run before edits are accepted, such as run Prettier on a specific file, or after edits, like write a type check on a specific file to make sure that it only accepts good and correct files.

You can create your own hooks via a `.claude/hooks.mjs` file, e.g. like below:

```jsx
// .claude/hooks.mjs
import { execSync } from 'child_process';
import path from 'path';

// Hook that runs before editing files
export async function preEdit({ filePath, oldContent, newContent }) {  
  // Check if editing TypeScript/JavaScript files
  if (filePath.match(/\.(ts|tsx|js|jsx)$/)) {
    // Ensure file is properly formatted before edit
    try {
      execSync(\`yarn prettier --check "${filePath}"\`, { stdio: 'pipe' });
    } catch (e) {
      console.log('⚠️  File needs formatting - will format after edit');
    }
  }
  
  // Prevent editing of certain protected files
  const protectedFiles = ['yarn.lock', 'package-lock.json', '.env.production', 'firebase.json'];
  const fileName = path.basename(filePath);
  if (protectedFiles.includes(fileName)) {
    throw new Error(\`❌ Cannot edit protected file: ${fileName}\`);
  }
  return { proceed: true };
}

// Hook that runs after editing files
export async function postEdit({ filePath, oldContent, newContent, success }) {
  if (!success) return;
  
  // Run type checking on TypeScript files
  if (filePath.match(/\.(ts|tsx)$/)) {
    try {
      execSync(\`npx tsc --noEmit --skipLibCheck "${filePath}"\`, { stdio: 'pipe' });
    } catch (e) {
      console.log('⚠️  TypeScript errors detected - please review');
    }
  }
}
```

### Creating custom slash commands

You can also add custom slash commands pretty easily. To add commands, just create a `.claude/commands` folder, add the command name as a file with a `.md` extension. You just write these in natural language and you can use the `$ARGUMENTS` string to place arguments into the prompt.

For example, if I want to output a test, I can create `.claude/commands/test.md`:

Then `/test MyButton` does exactly what you'd expect. You can even have subfolders - those we can access like `/builder/plugin` which would match a `builder` folder with a `plugin.md` file. That's how we can create a new Builder plugin super easily.

### Memory system

Another cool feature is you can use the `#` symbol to add memory super fast. Like "always use MUI components for new stuff," and it'll automatically save that to the most relevant file.

`CLAUDE.md` files can be hierarchical, so you can have one project-level and you can have one in nested directories. It looks at them all and prioritizes the most specific, the most nested when relevant.

You can also save this to global user memory preferences you want to apply everywhere, or local project memory that's specific to you and gets git-ignored. Add it to any of these files and it'll write it for you.

## When you want a normal UI

The terminal interface isn't always ideal. Sometimes you just want to click and highlight text like a normal person.

That's where our [Builder.io](https://builder.io/) extension comes in. You can launch a visual interface from your IDE that works exactly like Claude Code under the hood. We reverse-engineered it as closely as possible. You get a normal chat interface, live preview, and you can even switch to a Figma-style design mode to make visual edits.

<video></video>

Your whole team can use it — designers, PMs, whoever. They can create prototypes, clean up UIs, and submit PRs without needing to understand the terminal interface.

Internally at Builder, we've been using this to let our engineers focus on the hard engineering work while other teams handle UI details and pixel-perfect implementations.

Then, when our engineering team needs updates to PRs, we can just take the @builderio-bot and Claude will automatically address feedback and push up commits to address.

<video></video>

Go try it at [fusion.builder.io](https://fusion.builder.io/) and let me know your feedback

### A Figma-like editor for Cursor

Visually edit your code in your IDE or a browser

[Try Fusion](https://builder.io/signup) [Get a demo](https://builder.io/m/demo)

<video></video>