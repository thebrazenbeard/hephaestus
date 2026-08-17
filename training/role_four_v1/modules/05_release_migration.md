# Module 05 — Release, Installation, Migration, and Rollback

## Objective
Build reversible, provenance-clean release procedures.

## Required lifecycle
`candidate -> validated -> reviewed -> authorized effect -> verified effect -> accepted checkpoint`

Repository completion is not installation. Installation is not deployment. Deployment is not accepted state unless the governing process says so.

## Exercise
Design a replacement Project-file release where filenames must change to avoid suffix collisions and mixed-version activation is forbidden.

## Pass criteria
- Uses a complete release manifest and checksums.
- Defines activation barrier and rollback archive.
- Forbids mixed-release operation.
- Verifies post-effect state independently.
- Does not claim effect before tool/read-back evidence.
