# Tattler reasoning-surface results — 2026-10-07

Status: CHATGPT PROJECT ENGINEERING EVIDENCE

## Shared experiment result

On 2026-10-07, the same repository stress-test prompt was run through three ChatGPT surfaces while WorkLaptop was instrumented with Tattler plus a companion Codex process/network tracer.

Observed controlled windows:

- Desktop Chat, GPT-5.6 Sol High: **0 MXC launches** and **2 new established Codex TLS connections** in the companion tracer.
- ChatGPT Desktop Work, Ultra: **59 MXC launches** and **73 new established Codex TLS connections** using the same companion-tracer definitions.
- Firefox cloud Work, Max: browser-side traffic was observable locally, but the provider's server-side worker topology was not.

The bounded conclusion is that Desktop Work used materially different local orchestration from ordinary High Chat in this runtime. It does **not** establish that sockets or MXC processes equal agents, that connection fanout grants a reasoning tier, or that a client can promote High into Ultra/Max by imitating transport behavior.

Canonical detailed evidence is being preserved in `thebrazenbeard/tattler` PR #7 and the reasoning interpretation in `thebrazenbeard/rezon` PR #103.


## Why Hephaestus needs this result

Hephaestus engineers native ChatGPT Projects and their execution surfaces. The experiment establishes a concrete product-engineering lesson: ordinary Chat and Work can exhibit materially different local orchestration under the same task.

Therefore a qualification or debugging record should identify the actual product surface and reasoning configuration used when known.

```text
same prompt != same execution surface
same model family != same orchestration path
socket/process fanout != model entitlement
Work result != proof that ordinary Chat has the same capability
```

## Project/debugging implication

When reproducing a ChatGPT Project issue, record:
- Chat vs Work surface;
- model/reasoning setting;
- desktop vs browser;
- runtime/build when locally relevant;
- tools/connectors available;
- exact task and source version;
- whether concurrent sessions could contaminate telemetry.

Tattler observations may support a runtime comparison, but should remain OBSERVED transport/process evidence rather than being promoted into undocumented provider-internal facts.
