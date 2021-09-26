from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 tests=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tests = tests

    def execute(self, context):
        failed_test = []
        redshift_hook = PostgresHook(self.redshift_conn_id)
        self.log.info('Starting to check data quality in each tables')
        for test in self.tests:
            SQL = test.get('test_sql')
            expected_res = test.get('expected_res')
            res = redshift_hook.get_records(SQL)[0]
            if (res != expected_res):
                failed_test.append(SQL)
        if len(failed_test) != 0:
            self.log.info('Test Failed : ')
            for failed in failed_test:
                self.log.info(failed)
            raise ValueError('Data quality check failed')

        self.log.info('Data Quality all passed!')
