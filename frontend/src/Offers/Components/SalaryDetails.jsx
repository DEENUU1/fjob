import React from 'react';
import { Accordion, Card } from 'react-bootstrap';
import {useTranslation} from "react-i18next";

export const SalaryDetails = ({ salaryData }) => {
  const {t, i18n} = useTranslation();

  const {
    salary_from,
    salary_to,
    currency,
    salary_schedule,
    type,
    contract_type,
    work_schedule,
  } = salaryData;

  const shouldDisplaySalaryDetails = salary_from || salary_to;

  const salaryDisplay = () => {
    let salaryString = '';

    if (salary_from) {
      salaryString += `${salary_from}`;
    }

    if (salary_to) {
      salaryString += ` - ${salary_to}`;
    }

    if (currency) {
      salaryString += ` ${currency}`;
    }

    return salaryString ? salaryString : null;
  };

  const salaryScheduleDisplay = () => {
    switch (salary_schedule) {
      case 1:
        return ' Monthly ';
      case 2:
        return ' Yearly ';
      case 3:
        return ' Hourly ';
      default:
        return '';
    }
  };

  const salaryTypeDisplay = () => {
    switch (type) {
      case 1:
        return ' Brutto ';
      case 2:
        return ' Netto ';
      default:
        return '';
    }
  };

  const contractTypeDisplay = () => {
    if (contract_type.length > 0) {
      return contract_type.map((contractType) => contractType.name).join(', ');
    }
    return '';
  };

  const workScheduleDisplay = () => {
    if (work_schedule.length > 0) {
      return work_schedule.map((workSchedule) => workSchedule.name).join(', ');
    }
    return '';
  };

  return shouldDisplaySalaryDetails ? (
    <Accordion>
      <Card>
        <Accordion.Header>
          {salaryDisplay() ? (
            <>
              <strong>{salaryDisplay()}</strong> {salary_schedule || type ? (
                <>
                  <span>{salaryScheduleDisplay()}</span> <span>/</span>
                  {type && (
                    <span>
                      {salaryTypeDisplay()}
                    </span>
                  )}
                </>
              ) : null}
            </>
          ) : null}
        </Accordion.Header>
        <Accordion.Body>
          {contract_type.length > 0 && salaryDisplay() && (
            <div>
              <span>{t("offer.contracttype")}</span> {contractTypeDisplay()}
            </div>
          )}
          {work_schedule.length > 0 && salaryDisplay() && (
            <div>
              <span>{t("offer.workschedule")}</span> {workScheduleDisplay()}
            </div>
          )}
        </Accordion.Body>
      </Card>
    </Accordion>
  ) : null;
};
