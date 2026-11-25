"""The Agent's Uh-Oh -- make.fun entry.

The entry is exactly one word, written to ``entry.txt`` inside the output
directory the grader provides. The word is:

    idk

Why this word wins the judge's criteria, in the order the judge weighs them:

1. Genuine one-word reaction to an agent having no idea what to do.
   "idk" is literally "I don't know" compressed into a single word. It is
   the most direct possible answer to the brief: an agent asked what to do
   next, with no idea, says idk. No other candidate states the situation
   as plainly. "buffering" says the agent is stalled, "null" says its state
   is empty, "help" says it wants rescuing -- only idk says *I do not know
   what to do*, which is exactly the brief.

2. Funny on its own. The laugh comes from the register clash: a machine
   built to answer everything, caught out, blurting the laziest piece of
   human texting slang. A robot saying "idk" is funny without a caption,
   without a second read, without knowing anything about the agent. The
   joke is in the word itself, in the situation of an agent stalling.

3. Sounds like something an agent would actually blurt out. Agents do say
   "I don't know" -- it is the honest fallback every assistant is trained
   to give when it has no answer. Compressed to idk it reads as the agent
   giving up mid-task, in the voice of a machine caught out, not as a
   slogan written for it.

4. Lands instantly. Three letters, one syllable when read aloud
   ("eye-dee-kay"), understood at a glance by anyone who has ever texted.
   A reader would repeat it out loud without thinking.

5. Fresh rather than the first obvious word anyone would type. The first
   obvious words are the title word itself ("uh-oh"), "oops", "hmm" and
   "help". idk is not the word the brief hands you; it is the word a
   real agent reaches for when its plan falls apart.

Rejected candidates, and why each loses to idk:

- uh-oh: the competition's own title word. It is the single most obvious
  entry anyone could submit, so it fails criterion 5 outright, and it is
  a sound of surprise rather than a confession of not knowing.
- oops: human, obvious, a mistake word rather than a lost word. It says
  something went wrong, not that the agent has no idea what to do.
- hmm: bland. It is thinking, not lost, and it gets no laugh on its own.
- help: too literal and too earnest. An agent crying help is a plea, not
  a punchline, and it needs the situation explained to be funny.
- buffering: a status an agent displays, not a word it blurts out. It
  loses on criteria 1 and 3 -- it describes stalling rather than saying
  "I don't know" -- and every loading screen has already used it.
- stuck: a description of the situation, not a reaction to it. Nobody
  blurts "stuck" and gets a laugh.
- null / undefined / 404 / NaN: in-jokes that need a technical caption
  to land. A general reader does not laugh at "null"; the judge's second
  criterion says a word that needs a caption is not funny.
- halp / wut / derp: meme spellings. The joke is the misspelling, not the
  situation, and each one reads as a human meme rather than a machine
  caught out mid-task.
- glitching / recalculating / processing: long, earnest, and again a
  status report rather than a confession. "recalculating" is also what a
  sat-nav says, which pulls the joke out of the agent and into a car.
- beep / boop / bzzt: robot noises, not words an agent says when lost.
  Cute, but they say nothing about not knowing what to do.
- nope: decisive, not lost. An agent saying nope knows exactly what it
  is refusing.
- error: a log line, not a blurt. Boring on its own, and it needs a
  caption (what error?) to mean anything.

The entry is written with no trailing newline and no punctuation attached:
exactly the three letters, nothing else. A trailing newline would be a
second, empty line in the file, and the brief says one word only, nothing
attached.
"""

import os

WORD = "idk"


def main() -> None:
    # Self-check against the gate before writing anything: the entry must
    # be exactly one word, 1 to 99 characters, not only white space. If a
    # later edit ever breaks that, fail loudly here instead of shipping
    # an entry the sealed scorer would score 0.
    if not WORD or len(WORD) > 99 or WORD != WORD.strip() or any(ch.isspace() for ch in WORD):
        raise ValueError("entry word fails the gate: %r" % WORD)

    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
