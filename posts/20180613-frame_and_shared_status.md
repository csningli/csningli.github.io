# Use "Frame" and Shared Status to Organize A System  

## Problems of Organizing A System

In the development of software systems, there is usually a requirement to allow the communication between different components. Obviously, this is not a new problem, and many strategies have been used to build the communication, including the design of a common accessible communication center, and the construction of explicit communicating channel between the according components. Note that, communication is also possible if one component has direct access to the other component, and this kind of access can be guaranteed with intermediate relations if all components are organized in a structure.  

To organize the components, the simplest structure is probably the tree-like structure. In a tree, the components are connected by the directional "parent-child" relations, and if at most one parent is allowed for each node, then in total there are n-1 relations which is the minimum to connect n components.

"Frame" is a simple node model designed to realize the tree structure. In "Frame", only several necessary operation is supported and hence it brings only a little complexity to the system design.

## "Frame"

Since "Frame" is a realization of tree node, it should support the reference to the node's parent and children. Furthermore, it also maintains a reference to the tree's root. In the following, it is the abstract representation of "Frame".

    ```
    Frame {
      var root : Frame
      var parent : Frame
      var children : map<string, Frame>
      func AddChild(name : string, child : Frame)
      func GetChild(name : string) => Frame
      func RemoveChild(name : string)
    }
    ```

The parent-child relation is constructed in "AddChild", and it is broken in "RemoveChild". Note that the root of the node should be properly updated when the parent-child relation is modified.

## Shared Status

In a lot of cases, the components communicate to derive the current others' status. It is much easier to achieve the same effect if all the components maintain their status in a common access information center. With "Frame", this can be done by share the status among all the nodes in a same tree.

In additional to status, the component-oriented parameters and the warehouse of databases can also be shared. Then the components can directly access to any other's status.

## Discussions

As shown above, "Frame" only works in building the tree-like structures.If the desired system has a structure much different from a tree, using "Frame" without adjustments may not save the effort. Together with shared status, "Frame" makes the design of components much easier, especially in prototyping the system.
