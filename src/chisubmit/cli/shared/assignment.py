import click
from chisubmit.cli.common import pass_course, api_obj_set_attribute,\
    get_assignment_or_exit
import operator
from chisubmit.common.utils import convert_datetime_to_local
from chisubmit.common import CHISUBMIT_SUCCESS

@click.command(name="list")
@click.option('--ids', is_flag=True)
@click.option('--utc', is_flag=True)
@pass_course
@click.pass_context
def shared_assignment_list(ctx, course, ids, utc):
    assignments = course.assignments[:]
    assignments.sort(key=operator.attrgetter("deadline"))

    for assignment in assignments:
        if ids:
            print assignment.id
        else:
            if utc:
                deadline = assignment.deadline.isoformat(" ")
            else:
                deadline = convert_datetime_to_local(assignment.deadline).isoformat(" ")

            fields = [assignment.id, deadline, assignment.name]

            print "\t".join(fields)

    return CHISUBMIT_SUCCESS

@click.command(name="set-attribute")
@click.argument('assignment_id', type=str)
@click.argument('attr_name', type=str)
@click.argument('attr_value', type=str)
@pass_course
@click.pass_context
def shared_assignment_set_attribute(ctx, course, assignment_id, attr_name, attr_value):
    assignment = get_assignment_or_exit(ctx, course, assignment_id)
    
    api_obj_set_attribute(ctx, assignment, attr_name, attr_value)