import click
from cpp_stats import cpp_stats

@click.command()
@click.option('--report', default='report.xml', 
              help='Path to xml file where to store report.')
@click.argument('path_to_repo')
def main(path_to_repo, report):
    '''
    Main function of programm that calculates metrics for a given 
    C/C++ repository and stores report in XML file.
    
    Parameters:
    path_to_repo (str): Path to the repository.
    report (str): Path to xml file where to store report.
    '''
    stats = cpp_stats.CppStats(path_to_repo, True)
    with open(report, "w") as f:
        click.echo(stats.as_xml(), file=f)

if __name__ == "__main__":
    main()
