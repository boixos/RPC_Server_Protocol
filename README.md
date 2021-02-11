# CSE563: Internals of Application Servers

## Spring Semester 2021

## RPC Server Protocol

A problem statement was discussed in the class about how to design a complete RPC Protocol. In this
assignment we want you to implement the solution which was discussed in the class.

**Overview:**

- Server Side: Server is listening only over ftp on http.
- Client Side: Client wants to execute some functions defined on the server using RPC.

**Use Cases:**

- All the communications will be over ftp on http.
- Multiple clients can request services from the server at the same time.
- Any number of functions should be supported at server side and for each function there can be
    multiple versions (function will be differentiated on name not on function signature).
- Server-side developer should have an option to depreciate till a given version (including that) for
    a function.
- Appropriate basic error handling (In RPC Protocol part).

**Submission format:** <roll no>_lab 4 .zip

**Programming Language:** Python (mandatory)


