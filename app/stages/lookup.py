"""
Module definining an interface to MongoDB $count stage operation in aggrgation pipeline

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------

Last Updated (in this package) : 23/09/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup

Definition
----------------------------------

`Changed in version 5.1`

Performs a left outer join to a collection in the same database to filter in documents from the "joined" collection for processing. The
$lookup stage adds a new array field to each input document. The new array field contains the matching documents from the "joined" collection. The
$lookup stage passes these reshaped documents to the next stage.

Starting in MongoDB 5.1, $lookup works across sharded collections.

To combine elements from two different collections, use the $unionWith pipeline stage.

Syntax
----------------------------------
The $lookup stage has the following syntaxes

Equality Match with a Single Join Condition

To perform an equality match between a field from the input documents with a field from the documents of the "joined" collection, the
$lookup stage has this syntax:

    >>> {
            $lookup:
                {
                from: <collection to join>,
                localField: <field from the input documents>,
                foreignField: <field from the documents of the "from" collection>,
                as: <output array field>
                }
        }

The $lookup takes a document with these fields:

    * from : Specifies the collection in the same database to perform the join with.
             from is optional, you can use a $documents stage in a $lookup stage instead.
             For example, see [Use a $documents stage in a $lookup stage](https://www.mongodb.com/docs/manual/reference/operator/aggregation/documents/#std-label-documents-lookup-example)

    * localField : Specifies the fields from the documents input to the $lookup stage. $lookup performs an equality match on the localField to the ForeinField
                   from the documents of the from collection. If an input document does not contain the localField, the $looku^treats the field as having a value of null
                   for matching purposes

    * foreignField : Specifies the field from documents in the from collection. $lookup performs an equality match on the foreignField to the localField
                     from the input documents. If a document in the from collection does not contain the foreignField, the $lookup treats the value as null for
                     matching purposes

    * as : Speficies the name of the new array field to add to the input documents. The new array field contains the matching documents from the from collection.
           If the specified name already exists in the input document, the existing field is overwritten.

The operation would correspond to the following pseudo-SQL statement:

    >>> SELECT *, <output array field>
        FROM collection
        WHERE <output array field> IN (
            SELECT *
            FROM <collection to join>
            WHERE <foreignField> = <collection.localField>
        );

See these examples:

    * [Perform a Single Equality Join with](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#std-label-lookup-single-equality)
    * [Use $lookup with an Array](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#std-label-unwind-example)
    * [Use $lookup with $mergeObjects](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#std-label-lookup-mergeObjects)

Join Conditions and Subqueries on a Joined Collection

MongoDB 3.6 adds support for:

    * Executing a pipeline on a joined collection
    * Multiple join conditions
    * Correlated and uncorrelated subqueries

In MongoDB,
a correlated subquery is a pipelinein a $lookup stage that references document fields from a joined collection.
An uncorrelated subquery does not reference joined fields.

NOTE : Starting in MongoDB 5.0, for an uncorrelated subquery in a  $lookup
       pipeline stage containing a $sample stage, the $sampleRate operator, or the
       $rand operator, the subquery is always run again if repeated.
       Previously, depending on the subquery output size, either the subquery output was cached or the subquery was run again.

MongoDB correlated subqueries are comparable to SQL correlated subqueries, where the inner query references outer query values.
An SQL uncorrelated subquery does not reference outer query values.

MongoDB 5.0 also supports concise correlated subqueries.

To perform correlated and uncorrelated subqueries with two collections, and perform other join conditions besides a single equality match, use this
$lookup syntax:

    >>> {
            $lookup:
            {
                from: <joined collection>,
                let: { <var_1>: <expression>, …, <var_n>: <expression> },
                pipeline: [ <pipeline to run on joined collection> ],
                as: <output array field>
            }
        }

The $lookup stage accepts a document with these fields:

TODO : Add table here <VM, 23/09/2022>

The operation corresponds to this pseudo-SQL statement:

    >>> SELECT *, <output array field>
        FROM collection
        WHERE <output array field> IN (
            SELECT <documents as determined from the pipeline>
            FROM <collection to join>
            WHERE <pipeline>
        );

See the following examples:

    * [Perform Multiple Joins and a Correlated Subquery with $lookup](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#std-label-lookup-multiple-joins)
    * [Perform an Uncorrelated Subquery with $lookup](https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/#std-label-lookup-uncorrelated-subquery)

Correlated Subqueries Using Concise Syntax

`New in version 5.0.`

Starting in MongoDB 5.0, you can use a concise syntax for a correlated subquery.
Correlated subqueries reference document fields from a joined "foreign" collection and the "local" collection on which the
aggregate() method was run.

The following new concise syntax removes the requirement for an equality match on the foreign and local fields inside of an
$expr operator:

    >>> {
            $lookup:
                {
                    from: <foreign collection>,
                    localField: <field from local collection's documents>,
                    foreignField: <field from foreign collection's documents>,
                    let: { <var_1>: <expression>, …, <var_n>: <expression> },
                    pipeline: [ <pipeline to run> ],
                    as: <output array field>
                }
        }

The $lookup accepts a document with these fields:

TODO : Add table here <VM, 23/09/2022>

Behavior
------------------------------

Views and Collation

If performing an aggregation that involves multiple views, such as with
$lookup or $graphLookup, the views must have the same [collation](https://www.mongodb.com/docs/manual/reference/collation/).

Restrictions

`Changed in version 4.2.`

You cannot include the $outor the $merge stage in the $lookup stage.
That is, when specifying a pipeline for the joined collection, you cannot include either stage in the pipeline field.

>>> {
        $lookup:
        {
            from: <collection to join>,
            let: { <var_1>: <expression>, …, <var_n>: <expression> },
            pipeline: [ <pipeline to execute on the joined collection> ],  // Cannot include $out or $merge
            as: <output array field>
        }
    }

Atlas Search Support

Starting in MongoDB 6.0, you can specify the Atlas Search
$search or $searchMeta stage in the $lookup pipeline to search collections on the Atlas cluster.
The $search or the $searchMetastage must be the first stage inside the $lookup pipeline.

For example, when you Join Conditions and Subqueries on a Joined Collection
or run Correlated Subqueries Using Concise Syntax, you can specify
$search or $searchMeta inside the pipeline as shown below:

    >>> [{
            "$lookup": {
                "from": <joined collection>,
                localField: <field from the input documents>,
                foreignField: <field from the documents of the "from" collection>,
                "as": <output array field>,
                "pipeline": [{
                "$search": {
                    "<operator>": {
                    <operator-specification>
                    }
                },
                ...
                }]
            }
        }]

    >>> [{
            "$lookup": {
                "from": <joined collection>,
                localField: <field from the input documents>,
                foreignField: <field from the documents of the "from" collection>,
                "as": <output array field>,
                "pipeline": [{
                "$searchMeta": {
                    "<collector>": {
                    <collector-specification>
                    }
                },
                ...
                }]
            }
        }]

To see an example of $lookup with $search, see the Atlas Search tutorial
[Run an Atlas Search $search Query Using $lookup](https://www.mongodb.com/docs/atlas/atlas-search/tutorial/lookup-with-search/)

Sharded Collections

Starting in MongoDB 5.1, you can specify sharded collections in the from parameter of $lookup stages.

Slot-Based Query Execution Engine

Starting in version 6.0, MongoDB can use the slot-based execution query engine to execute $lookup
stages if all preceding stages in the pipeline can also be executed by the slot-based engine and none of the following conditions are true:

    * The $lookup operation executes a pipeline on a joined collection. To see an example of this kind of operation,
      see Join Conditions and Subqueries on a Joined Collection above.

    * The $lookup's localField or foreignField specify numeric components. For example: { localField: "restaurant.0.review" }.

    * The from field of any $lookup in the pipeline specifies a view or sharded collection.

For more information, see [$lookup Optimization](https://www.mongodb.com/docs/manual/core/aggregation-pipeline-optimization/#std-label-agg-lookup-optimization-sbe).

"""

from pydantic import root_validator, Field
from app.stages.stage import Stage

class Lookup(Stage):
    """
    Creates a lookup statement for an aggregation pipeline lookup stage.

    Attributes
    ----------------------------
        - right / from (official MongoDB name), str : foreign collection
        - left_on / local_field (official MongoDB name)), str | None : field of the current collection to join on
        - right_on / foreign_field (official MongoDB name), str | None : field of the foreign collection to join on
        - let, dict | None : variables to be used in the inner pipeline
        - pipeline, list[dict] | None : pipeline to run on the foreign collection.
        - as, str : name of the field containing the matches from the foreign collection
    """

    right : str = Field(..., alias="from")
    on : str | None #  shortcut for when left_on is the same than right_on
    left_on : str | None = Field(...,alias="local_field")
    right_on : str | None = Field(..., alias="foreign_field")
    name : str | None = Field(...,alias="as")
    type_ : str # internal variable to know the type of join (simple, correlated, uncorrelated)

    # Subquery fields
    # ---------------------
    let : dict | None
    pipeline : list[dict] | None

    @root_validator(pre=True)
    @classmethod
    def generate_statement(cls, values:dict)->dict:
        """Generates statement from attributes"""

        # Retrieving the values passed
        # ----------------------------------
        right = values.get("right") # necessary to use an alias here as from is a python keyword
        on = values.get("on") # pylint: disable=invalid-name
        local_field = values.get("local_field")
        foreign_field = values.get("foreign_field")
        let = values.get("let")
        pipeline = values.get("pipeline")

        name = values.get("name") # necessary to use an alias here as as is a python keyword

        # Handling aliases
        # ----------------------------------
        if not right:
            right = values.get("from")

        if not local_field:
            local_field = values.get("left_on")

        if not foreign_field:
            foreign_field = values.get("right_on")

        if on:
            local_field = foreign_field = on

        if not name:
            name = values.get("as")

        # Validates combination of argument
        # ------------------------------------
        if right and local_field and foreign_field and not(let or pipeline is None):
            # in a subquery to select all on the foreign collection
            # pipeline can be an empty list which is falsy
            type_ = "simple"

        elif let and pipeline is not None and not(local_field or foreign_field):
            type_ =  "uncorrelated"

        elif let and pipeline is None and local_field and foreign_field:
            type_ = "correlated"

        else:
            raise TypeError("Incompatible combination of arguments")

        values["type_"] = type_

        # Generate statement:
        # -----------------------------------------------
        if type_ == "simple":
            statement = {
                "$lookup":{
                    "from":right,
                    "localField":local_field,
                    "foreignField":foreign_field,
                    "as":name
                }
            }
        elif type_ == "uncorrelated":
            statement = {
                "$lookup":{
                    "from":right,
                    "let":let,
                    "pipeline":pipeline,
                    "as":name
                }
            }
        else: # should be correlated case
            statement = {
                "$lookup":{
                    "from":right,
                    "localField":local_field,
                    "foreignField":foreign_field,
                    "let":let,
                    "pipeline":pipeline,
                    "as":name
                }
            }

        values["statement"] = statement

        return values
